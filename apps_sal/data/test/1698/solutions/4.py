(n, k) = list(map(int, input().split()))
e = 1
ans = 0
p = sorted(list(map(int, input().split())), reverse=True)
for i in range(0, n, k):
    ans += max(p[i:i + k]) * 2 - 2
print(ans)
