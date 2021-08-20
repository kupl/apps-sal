(N, L) = list(map(int, input().split()))
A = 0
a = 1000
for i in range(1, N + 1):
    x = L + i - 1
    A += x
    if abs(x) < a:
        a = abs(x)
if A >= 0:
    print(A - a)
else:
    print(A + a)
