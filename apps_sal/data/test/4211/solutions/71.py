N = int(input())
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    if i == 0:
        ans += B[i]
    elif i == N - 1:
        ans += B[i - 1]
    else:
        ans += min(B[i], B[i - 1])
print(ans)
