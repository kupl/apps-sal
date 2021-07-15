class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def powerof(num, memo):
            step = 0
            n = num
            while n > 1:
                if n in memo:
                    return step + memo[n]
                if n % 2 == 0:
                    n = n // 2
                else:
                    n = 3*n+1
                step += 1
            memo[num] = step
            return step
        mheap = []
        memo = {}
        for n in range(lo, hi+1):
            mheap.append([powerof(n, memo), n])
        heapq.heapify(mheap)
        return heapq.nsmallest(k, mheap)[-1][1]
