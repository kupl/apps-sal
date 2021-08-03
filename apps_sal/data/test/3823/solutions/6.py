N = int(input())
n = N
A = list(map(float, input().strip().split(' ')))
z = 0
for i in range(len(A)):
    A[i] = round(A[i], 3) - int(A[i])
    if A[i] == 0:
        z += 1
# print(A)
ANS = sum(A)
# print(ANS)
ans = 10**10
for j in range(n - z, n + 1):
    ans = min(ans, abs(ANS - j))

print("%.3f" % ans)
