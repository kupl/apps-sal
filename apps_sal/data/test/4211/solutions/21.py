n = int(input())
b = [10**6] + list(map(int, input().split())) + [10**6]

ans = 0
for i in range(1, n+1):
    ans += min(b[i-1], b[i])
print(ans)
