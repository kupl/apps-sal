from functools import wraps


class Solution:

    def longestCommonSubsequence(self, text1, text2):

        def cache_decorator(f):
            _cache = {}

            @wraps(f)
            def new_f(*args):
                if args not in _cache:
                    _cache[args] = f(*args)
                return _cache[args]
            return new_f

        @cache_decorator
        def compute(x, y):
            if x == len(text1):
                return 0
            if y == len(text2):
                return 0
            if text1[x] == text2[y]:
                return 1 + compute(x + 1, y + 1)
            return max([compute(x + 1, y), compute(x, y + 1)])
        return compute(0, 0)
