class Solution:

    def countTriplets(self, A: List[int]) -> int:
        counters = [0] * (1 << 16)
        counters[0] = len(A)
        for num in A:
            mask = ~num & (1 << 16) - 1
            sm = mask
            while sm != 0:
                counters[sm] += 1
                sm = sm - 1 & mask
        return sum((counters[num1 & num2] for num1 in A for num2 in A))
