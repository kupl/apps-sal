n = int(input())
w = list(map(int, input().split()))

ans = 99

for i in range(1, n):
    tmp = abs(sum(w[:i]) - sum(w[i:]))
    ans = min(tmp, ans)

print(ans)
