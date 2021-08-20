class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        used = [False] * len(A)
        A.sort(key=lambda n: abs(n))
        bank = collections.Counter(A)
        for num in A:
            if bank[num] == 0:
                continue
            bank[num] -= 1
            if bank.get(2 * num, 0) == 0:
                return False
            bank[2 * num] -= 1
        return True
