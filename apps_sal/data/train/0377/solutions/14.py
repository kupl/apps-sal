import heapq


class Solution:

    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:

        def gcd(i, j):
            if i > j:
                (i, j) = (j, i)
            while i != 0:
                j %= i
                (i, j) = (j, i)
            return j
        common_mult = A * B // gcd(A, B)
        c_count = common_mult // A + common_mult // B - 1
        unit_count = N // c_count
        remainder = N % c_count
        base = unit_count * common_mult % (10 ** 9 + 7)
        if remainder == 0:
            return base
        heap = [A, B]
        heapq.heapify(heap)
        while heap:
            curr = heapq.heappop(heap)
            remainder -= 1
            if remainder == 0:
                return (base + curr) % (10 ** 9 + 7)
            if curr % A == 0:
                heapq.heappush(heap, curr + A)
            else:
                heapq.heappush(heap, curr + B)
