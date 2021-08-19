(n, m) = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
p = 1
for i in a:
    ans += [i - p, i - p + n][i < p]
    p = i
print(ans)
