import collections


def f():
    return map(int, input().split())


N = int(input())
(*A,) = f()
Q = int(input())
BC = [f() for _ in range(Q)]
c = collections.Counter(A)
s = sum(A)
for (i, j) in BC:
    v = c[i]
    s += v * (j - i)
    print(s)
    c[j] += v
    c[i] = 0
