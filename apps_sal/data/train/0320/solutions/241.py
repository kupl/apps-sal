class Solution:

    def minOperations(self, nums: List[int]) -> int:
        odds: List[int] = [n for n in nums if n % 2 == 1]
        evens: Set[int] = [n for n in nums if n != 0 and n % 2 == 0]
        new: List[int] = []
        n: int = 0
        n_ops: int = 0
        while len(odds) > 0 or len(evens) > 0:
            if len(odds) > 0:
                n = odds.pop() - 1
                if n > 0:
                    evens.append(n)
            else:
                new = [n // 2 for n in evens]
                odds = [n for n in new if n % 2 == 1]
                evens = [n for n in new if n % 2 == 0]
            n_ops += 1
        return n_ops
