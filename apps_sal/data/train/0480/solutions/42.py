def memoize(f):
    d = {}

    def memoized_f(*args):
        if args not in d:
            d[args] = f(*args)
        return d[args]
    return memoized_f


@memoize
def numWaysHelper(steps, arrLen, position):
    if position < 0 or position >= arrLen:
        return 0
    if steps == 0:
        if position == 0:
            return 1
        return 0
    big_num = 10 ** 9 + 7
    return (numWaysHelper(steps - 1, arrLen, position - 1) +
            numWaysHelper(steps - 1, arrLen, position) +
            numWaysHelper(steps - 1, arrLen, position + 1)) % big_num


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        return numWaysHelper(steps, arrLen, 0)
