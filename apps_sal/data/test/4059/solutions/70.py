N = int(input())
ans = 0
for A in range(1, N):
    ans += (N - 1) // A
print(ans)
