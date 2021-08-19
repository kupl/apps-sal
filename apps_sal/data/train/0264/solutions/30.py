class Solution:
    # I believe this problem is equivalent to SAT with weighted variables so I
    # won't try to beat exp complexity. The state space is 2^16 configurations
    # large so exp complexity shouldn't be a problem.

    def maxLength(self, arr):
        # From python docs: https://docs.python.org/3/library/itertools.html#itertools-recipes
        def powerset(iterable):
            import itertools
            s = list(iterable)
            return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))

        result = 0
        for subset in powerset(arr):
            candidate = ''.join(subset)
            if (len(candidate) > result and len(candidate) == len(set(candidate))):
                result = len(candidate)

        return result
