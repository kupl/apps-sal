import collections
N = int(input())
(*A,) = map(int, input().split())
Q = int(input())
BC = [list(map(int, input().split())) for _ in range(Q)]
c = collections.Counter(A)
s = sum(A)
for (i, j) in BC:
    v = c[i]
    s += v * (j - i)
    print(s)
    c[j] += v
    c[i] = 0
