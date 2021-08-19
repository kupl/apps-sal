class Solution:

    def numSplits(self, s: str) -> int:
        dic_b = {}
        for i in s[1:]:
            if i not in dic_b:
                dic_b[i] = 1
            else:
                dic_b[i] += 1
        b_count = len(dic_b)
        a = list(s[:1])
        a_count = 1
        count = int(b_count == a_count)
        ix = 1
        while ix < len(s):
            if s[ix] not in a:
                a_count += 1
            a.append(s[ix])
            dic_b[s[ix]] -= 1
            if dic_b[s[ix]] == 0:
                b_count -= 1
            count += int(a_count == b_count)
            ix += 1
        return count
