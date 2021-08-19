N = int(input())
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    if i == 0:
        ans += B[0]
    elif i == N - 1:
        ans += B[N - 2]
    else:
        ans += min(B[i - 1], B[i])
print(ans)
