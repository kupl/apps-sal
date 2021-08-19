class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 0
            d[i] += 1
        d = list(sorted(d.items(), key=lambda kv: kv[1], reverse=True))
        sum = 0
        cnt = 0
        for i in range(len(d)):
            if sum >= len(arr) / 2:
                break
            else:
                sum = sum + d[i][1]
                cnt += 1
        return cnt
