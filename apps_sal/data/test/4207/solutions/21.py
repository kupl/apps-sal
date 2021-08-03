from fractions import gcd
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
c = {}
q = 0
for i in range(N):
    if A[i] != 0:
        if B[i] != 0:
            g = gcd(B[i], A[i])
            k = (B[i] // g, A[i] // g)
        else:
            k = (0, 0)
        if k in c:
            c[k] += 1
        else:
            c[k] = 1
    else:
        if B[i] == 0:
            q += 1
if c:
    print(max(c.values()) + q)
else:
    print(q)
