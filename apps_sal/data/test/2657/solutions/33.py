N = int(input())
A = list(map(int, input().split()))
A.sort()
n = A[-1]

d = n
r = -1
for a in A[:-1]:
    if n % 2 == 0:
        t = abs(a - n // 2)
        if t < d:
            d = t
            r = a
    else:
        t = min(abs(a - n // 2), abs(a - (n // 2 + 1)))
        if t < d:
            d = t
            r = a
print(n, r)
