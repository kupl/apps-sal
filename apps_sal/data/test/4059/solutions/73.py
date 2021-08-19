N = int(input())
ans = 0
for a in range(1, N):
    n = (N - 1) // a
    ans += n
print(ans)
