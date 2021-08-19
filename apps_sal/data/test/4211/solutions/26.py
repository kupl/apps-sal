N = int(input())
B = list(map(int, input().split()))
ans = B[0] + B[N - 2]
for i in range(1, N - 1):
    ans += min(B[i - 1], B[i])
print(ans)
