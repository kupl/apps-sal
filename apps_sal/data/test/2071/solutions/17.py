n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = [b[n-1]]
B = [a[n-1]]
S = [a[n-1] + b[n-1]]
for i in range(1, n):
    A.append(A[-1] + S[-1] + b[n - i - 1] * (2*i + 1))
    B.append(B[-1] + S[-1] + a[n - i - 1] * (2*i + 1))
    S.append(S[-1] + a[n - i - 1] + b[n - i - 1])

A = A[::-1]
B = B[::-1]
S = S[::-1]

m = 0
s = 0
for i in range(n):
    if i % 2 == 0:
        m = max(m, s + A[i] + S[i] * 2*i)
        s += 2*i*a[i] + (2*i + 1)*b[i]
    
    else:
        m = max(m, s + B[i] + S[i] * 2*i)
        s += 2*i*b[i] + (2*i + 1)*a[i]

print(m)
