N, M = map(int, input().split())
A = []
for i in range(N):
    a, b = map(int, input().split())
    A.append([a, b])

A.sort()
S = 0
for i, j in A:
    if M - j >= 0:
        S += i * j
        M -= j
    else:
        S += M * i
        break
print(S)
