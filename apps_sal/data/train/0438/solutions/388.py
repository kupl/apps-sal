class Solution:

    def findLatestStep(self, arr, m):
        l = [[] for _ in range(len(arr) + 2)]
        step = 1
        cnt = 0
        ans = -1
        for idx in arr:
            l[idx].append(1)
            if l[idx][0] == m:
                cnt += 1
            if l[idx - 1] and l[idx + 1]:
                if l[idx - 1][0] == m:
                    cnt -= 1
                if l[idx + 1][0] == m:
                    cnt -= 1
                if l[idx][0] == m:
                    cnt -= 1
                _sum = l[idx - 1][0] + l[idx][0] + l[idx + 1][0]
                i = 1
                while l[idx - i]:
                    l[idx - i] = l[idx]
                    i += 1
                i = 1
                while l[idx + i]:
                    l[idx + i] = l[idx]
                    i += 1
                l[idx].pop()
                l[idx].append(_sum)
                if l[idx][0] == m:
                    cnt += 1
            elif l[idx - 1]:
                if l[idx - 1][0] == m:
                    cnt -= 1
                if l[idx][0] == m:
                    cnt -= 1
                _sum = l[idx - 1][0] + l[idx][0]
                l[idx] = l[idx - 1]
                l[idx].pop()
                l[idx].append(_sum)
                if l[idx][0] == m:
                    cnt += 1
            elif l[idx + 1]:
                if l[idx + 1][0] == m:
                    cnt -= 1
                if l[idx][0] == m:
                    cnt -= 1
                _sum = l[idx + 1][0] + l[idx][0]
                l[idx] = l[idx + 1]
                l[idx].pop()
                l[idx].append(_sum)
                if l[idx][0] == m:
                    cnt += 1
            if cnt > 0:
                ans = step
            step += 1
        return ans
