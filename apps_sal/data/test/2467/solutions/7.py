class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        import functools;
        return [c for c in functools.reduce(lambda nexts, _: [next_ + [first] for next_ in nexts for first in range(next_[-1] + 1 if next_ else 1, 10)], range(k), [[]]) if sum(c) == n]
