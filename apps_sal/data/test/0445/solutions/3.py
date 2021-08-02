import math

N = 2000001
sq = math.floor(N ** 0.5)
isprime = [True] * N
for p in range(2, N):
    if isprime[p]:
        for i in range(p**2, N, p):
            isprime[i] = False


def solve():
    n = int(input())
    A = [int(x) for x in input().split()]
    odd = list([x for x in A if x % 2])
    even = list([x for x in A if x % 2 == 0])
    k = odd.count(1)
    res = None
    if k > 0:
        for i in even:
            if isprime[i + 1]:
                res = [1] * k + [i]
                return res
        if k > 1:
            res = [1] * k
            return res
    if res is None:
        for i in odd:
            for j in even:
                if isprime[i + j]:
                    res = [i, j]
                    return res
    return [A[0]]


res = solve()
print(len(res))
print(' '.join(map(str, res)))
