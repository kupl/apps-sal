N, X = list(map(int, input().split()))
L = list(map(int, input().split()))
x = 0
ans = 1
for i in range(N):
    x += L[i]
    if x <= X:
        ans += 1
print(ans)
