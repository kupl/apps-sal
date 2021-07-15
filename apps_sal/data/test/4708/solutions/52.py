N = int(input())
K = int(input())
X = int(input())
Y = int(input())

ans = 0

for i in range(N):
    if i + 1 <= K:
        ans += X
    else:
        ans += Y
print(ans)
