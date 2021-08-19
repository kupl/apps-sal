n = int(input())
A = list(map(int, input().split()))
A.sort()
ANS = 0
for i in range(n // 2):
    ANS += A[2 * i + 1] - A[2 * i]
print(ANS)
