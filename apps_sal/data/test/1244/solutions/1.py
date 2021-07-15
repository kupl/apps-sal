n = int(input())
A = list(map(int, input().split()))
P = [0] * 1000
for i in range(n):
    P[A[i] - 1] += 1
ans = 0
for i in range(1000):
    if (P[i] > (n + 1) / 2):
        ans = 1
if (ans):
    print("NO")
else:
    print("YES")
