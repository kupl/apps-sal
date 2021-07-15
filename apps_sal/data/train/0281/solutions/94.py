class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        total = [0]
        # print(count)
        for i in range(len(s)):
            if ord(s[i]) > ord(t[i]):
                # print('case {} {}'.format(s[i], t[i]))
                x = 122 - ord(s[i]) + ord(t[i]) - 96
            else:
                x = ord(t[i]) - ord(s[i])
            # print(\"({} {})\".format(x,i))
            if x != 0:
                if x not in count:
                    count[x] = 0
                if count[x] * 26 + x:
                    max = count[x] * 26 + x
                    if max > k:
                        return False
                count[x] += 1
        # print(max(total))
        return True
