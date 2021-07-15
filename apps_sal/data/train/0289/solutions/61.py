class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        import heapq
        n = len(A)
        def get_subsum(L):
            Lsum = [sum(A[:L])]
            for i in range(1, n-L+1):
                Lsum.append(Lsum[i-1] + A[i+L-1] - A[i-1])
            return [(s, i) for i, s in enumerate(Lsum)]
        Lsum = get_subsum(L)
        # print(Lsum)
        Lsum.sort(reverse=True)
        Msum = get_subsum(M)
        # print(Msum)
        Msum.sort(reverse=True)
        def overlap(i, j, L=L, M=M):
            #i, i+L-1
            #j, j+M-1
            return j <= i < j+M or i <= j < i + L
        i = j = 0
        Llen = len(Lsum)
        Mlen = len(Msum)
        visited = set()
        stack = []
        heapq.heappush(stack, (0, (0,0)))
        while stack:
            _, (i, j) = heapq.heappop(stack)
            # visited.add((i,j))
            # print(i, j, Lsum[i], Msum[j])
            if not overlap(Lsum[i][1], Msum[j][1]):
                return Lsum[i][0] + Msum[j][0]
            if i < Llen - 1 and not (i+1, j) in visited:
                visited.add((i+1,j))
                heapq.heappush(stack, (-(Lsum[i+1][0] + Msum[j][0]), (i+1, j)))
            if j < Mlen - 1 and not (i,j+1) in visited:
                visited.add((i,j+1))
                heapq.heappush(stack, (-(Lsum[i][0] + Msum[j+1][0]), (i, j+1)))

