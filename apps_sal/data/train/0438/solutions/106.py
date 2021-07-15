class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        count = [0]*(n + 1)
        length = [0]*(n + 1)
        p = list(range(1 + n))
        cur = [0]*(n + 2)
        
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
        def union(x, y):
            t1, t2 = find(x), find(y)
            a, b = length[t1], length[t2]
            p[t1] = t2
            length[t2] = a + b
            count[a] -= 1
            count[b] -= 1
            count[a + b] += 1
        ans = -1
        for i, x in enumerate(arr):
            #print('in', i, x, cur, length, count)
            cur[x] += 1
            length[x] = 1
            count[1] += 1
            if cur[x - 1]:
                union(x, x - 1)
            if cur[x + 1]:
                union(x, x + 1)
            if count[m]:
                ans = i + 1
        return ans

