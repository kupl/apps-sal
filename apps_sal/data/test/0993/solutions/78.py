import numpy
(N, M) = map(int, input().split())
A = list(map(int, input().split()))
D = list(numpy.cumsum(A))
C = {}
D.append(0)
for i in D:
    d = i % M
    if d not in C:
        C[d] = 1
    else:
        C[d] += 1
ans = 0
for i in C.values():
    ans += i * (i - 1) // 2
print(ans)
