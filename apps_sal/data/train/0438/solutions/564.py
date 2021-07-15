class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        d = defaultdict(int)
        ans = 0
        n = len(arr)
        l = [-1]*n
        r = [-1]*n
        for i in range(n):
            x = y = arr[i]-1
            if x and l[x-1] != -1:
                d[(x-1)-l[x-1]+1] -= 1
                x = l[x-1]
            if y < n-1 and r[y+1] != -1:
                d[r[y+1]-(y+1)+1] -= 1
                y = r[y+1]
            d[y-x+1] += 1
            if d[m]:
                ans = i+1
            l[y] = x
            r[x] = y
        return ans if ans else -1
