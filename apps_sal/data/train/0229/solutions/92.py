class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:

        # Divide an conquer
        # Sort items according to their magnitude
        # For each item, make sure it's double exists later in the list
        # When a double is used, mark it with a mask

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
