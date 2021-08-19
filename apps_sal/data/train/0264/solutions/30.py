class Solution:

    def maxLength(self, arr):

        def powerset(iterable):
            import itertools
            s = list(iterable)
            return itertools.chain.from_iterable((itertools.combinations(s, r) for r in range(len(s) + 1)))
        result = 0
        for subset in powerset(arr):
            candidate = ''.join(subset)
            if len(candidate) > result and len(candidate) == len(set(candidate)):
                result = len(candidate)
        return result
