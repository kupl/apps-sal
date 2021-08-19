# imports
import operator as ops  # lt, le, eq, ne, ge, gt,  xor  notit, lshift, rshift,      neg, add, mul, sub,
from operator import __or__ as orit
from operator import __abs__ as absit
from operator import __not__ as notit
from functools import reduce, partial
from itertools import permutations as perms, product as prod, combinations_with_replacement as rcombos
from itertools import starmap, tee, chain, filterfalse, combinations as combos
from fractions import Fraction
from math import pi as PI, e as E
from math import ceil, floor, factorial, fsum, isinf, exp, log, log10, log2, isfinite, sqrt
from collections import Counter, defaultdict, deque
import sys
sys.setrecursionlimit(30000)


#PI, E, PHI, INF
PHI, PHI2 = (1 + 5 ** 0.5) / 2, (5 ** 0.5 - 1) / 2
INF = float('inf')

# structures


class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

# Bit Manipulation
# <<, >>, bin(), int(s, 2)


def setBit(x, offset):
    return x | 1 << offset  # RHS: mask


def clearBit(x, offset):
    return x & ~(1 << offset)  # RHS: mask


def getBit(x, offset):
    return 1 if testBit(x, offset) > 0 else 0


def testBit(x, offset):
    return x & 1 << offset  # RHS: mask


def flipBitAt(x, offset):
    return x ^ 1 << offset  # RHS: mask


def flipBits(x, length=-1):  # default: x.bit_length() - 1
    length = x.bit_length() - 1 if length == -1 else length
    return x ^ (1 << length) - 1


def numBits(x):
    return x.bit_length()  # int.bit_length()


def countOnes(x):
    return bin(x).count('1')


def countZeros(x, length=-1):
    length = x.bit_length() if length == -1 else length
    return length - countOnes(x)

# IO


def getList(tcast=str):
    return [tcast(x) for x in input().strip().split(' ')]


def getItems(*tcast):
    return map(lambda f, x: f(x), tcast, getList())


def getVal(tcast=str):
    return tcast(input().strip())


def getMatrix(r, tcast=str):
    return [getList(tcast) for row in range(r)]

# Math


def isOdd(n):
    return n & 1 > 0


def isEven(n):
    return not n & 1


def numDigits(n):
    return len(str(n)) - (1 if n < 0 else 0)


def getRecip(f):
    return Fraction(f.denominator, f.numerator)


def _gcd(a, b):
    while b:  # is not zero
        a, b = b, a % b
    return a


def gcd(*xs):
    nums = xs[0] if type(xs[0]) == list else list(xs)
    cur = nums[0]
    for n in nums[1:]:
        if cur == 1:
            return cur
        cur = _gcd(cur, n)
    return cur


def _lcm(a, b):
    return (a // gcd(a, b)) * b


def lcm(*xs):
    nums = xs[0] if type(xs[0]) == list else list(xs)
    cur = nums[0]
    for n in nums[1:]:
        cur = _lcm(cur, n)
    return cur


def primesUpto(n):
    isp = [True] * (n + 1)
    isp[0], isp[1] = False, False
    primes = []
    for i, x in enumerate(isp):  # for each number
        if x:  # found a prime
            primes.append(i)
            mults = i * i
            while mults <= n:
                isp[mults] = False
                mults += i
    return primes


def primeFactor(n):  # without a sieve
    factors = Counter()
    while not n & 1:
        factors[2] += 1
        n >>= 1
    trynum = 3
    while trynum <= ceil(sqrt(n)):  # just in case
        while n % trynum == 0:
            factors[trynum] += 1
            n //= trynum
        trynum += 2
    if n != 1:
        factors[n] += 1
    return factors


def isPrime(n):  # num -> boolean
    if n & 1 and n >= 2:
        trynum = 3
        limit = ceil(sqrt(n))
        while trynum < limit:
            if n % trynum == 0:
                return False
            trynum += 2
        else:
            return True
    else:
        return False


def nthFib(n):
    if n <= 2:
        return 1
    else:
        a, b = 1, 1
        while n > 2:
            a, b = b, a + b
            n -= 1
        return b

# Iteration


def zipNWith(f, *x):  # xs, ys, ... zs -> elementwise f -> os #return map(lambda *y: f(y), x) #list way: [f(y) for y in zip(*xs)]
    return (f(y) for y in zip(*x))


def zipWith(f, xs, ys):
    return (f(x, y) for x, y in zip(xs, ys))


def flatten(xs):
    return reduce(ops.concat, xs)


def quantify(pred, it):
    return sum(map(pred, it))


def dotproduct(xs, ys):
    return sum(map(ops.mul, xs, ys))


def pairwise(it):
    a, b = tee(it)
    next(b, None)
    return zip(a, b)


def bipartition(pred, it):
    t, f = tee(it)
    return filter(pred, t), filterfalse(pred, f)


def powerset(it):
    s = list(it)
    return chain.from_iterable(combos(s, r) for r in range(len(s) + 1))


# Input
# Body
# Output
n = getVal(int)
nums = getList(int)
nums.sort()
mid = (n - 1) // 2
print(nums[mid])
