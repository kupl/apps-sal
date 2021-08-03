class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        A, B = list(A), list(B)
        res = float('inf')
        q = [(0, 0, B)]  # (i) index, (k) swaps made, (B) current list

        while q:

            i, k, B = heapq.heappop(q)
            i = -i

            if k >= res:
                continue

            while (i < len(B)) and (B[i] == A[i]):
                i += 1

            if i == len(B):
                res = min(res, k)
                continue

            target = A[i]
            j = i + 1
            while j < len(B):
                if B[j] == target:
                    heapq.heappush(q, (-(i + 1), k + 1, B[:j] + [B[i]] + B[j + 1:]))
                j += 1

        return res
