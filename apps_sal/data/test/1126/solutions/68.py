(n, x, m) = list(map(int, input().split()))
A = [x]
M = [0] * m
while True:
    x = pow(x, 2, m)
    if M[x] == 1:
        break
    A.append(x)
    M[x] = 1
s = A.index(x)
shuki = len(A) - s
if n <= s:
    print(sum(A[:n]))
else:
    n -= s
    su = sum(A[s:])
    print(n // shuki * su + sum(A[s:s + n % shuki]) + sum(A[:s]))
