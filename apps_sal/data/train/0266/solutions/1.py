class Solution:

    def numSplits(self, s: str) -> int:
        index_one = 0
        index_two = 0
        set_one = set()
        set_two = set()
        s_r = s[::-1]
        for i in range(len(s)):
            print((i, len(set(s[:i + 1])), len(set(s[i + 1:]))))
            if len(set(s[:i + 1])) == len(set(s[i + 1:])):
                index_one = i
                break
            else:
                set_one.add(s[i])
        for i in range(len(s_r)):
            print((i, len(set(s_r[:i + 1])), len(set(s_r[i + 1:]))))
            if len(set(s_r[:i + 1])) == len(set(s_r[i + 1:])):
                print(i)
                index_two = len(s) - i - 1
                break
            else:
                set_two.add(s_r[i])
        print((index_one, index_two))
        return index_two - index_one
