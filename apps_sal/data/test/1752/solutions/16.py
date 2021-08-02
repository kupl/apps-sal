n = int(input())
A = list(map(int, input().split()))

A.sort()
ANS = [-1] * n

for i in range(n):
    if i % 2 == 0:
        ANS[i // 2] = A[i]
    else:
        ANS[-(i + 1) // 2] = A[i]

for a in ANS:
    print(a, end=" ")
