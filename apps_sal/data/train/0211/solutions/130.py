class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)-1
        ans = 1
        for i in range(1 << n):
            subs = set()
            start = 0
            flag = False
            for j in range(n):
                if 1 << j & i:
                    tmp = s[start:j+1]
                    if tmp in subs:
                        flag = True
                        break
                    subs.add(tmp)
                    start = j+1
            if flag:
                continue
            tmp = s[start:]
            if tmp in subs:
                continue
            # print(subs, i)
            ans = max(ans, len(subs)+1)
        return ans
