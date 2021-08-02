from math import factorial

N, A, B = list(map(int, input().split()))
V = [int(i) for i in input().split()]
V.sort(reverse=True)

a = 0
for i in range(A):
    a += V[i]
a /= A
print(a)

c = 0

if V[0] != V[A - 1]:
    r = 0
    while True:
        r += 1
        if V[A - 1 - r] != V[A - 1]:
            break
    n = 0
    while True:
        if A + n > N - 1:
            break
        if V[A + n] != V[A - 1]:
            break
        n += 1
    n += r
    c = round(factorial(n) / factorial(r) / factorial(n - r))

else:
    n = 0
    while True:
        n += 1
        if n > N - 1:
            break
        if V[n] != V[0]:
            break
    B = min(B, n)
    for i in range(B - A + 1):
        c += round(factorial(n) / factorial(A + i) / factorial(n - A - i))

print(c)
