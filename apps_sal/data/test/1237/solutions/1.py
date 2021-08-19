3
(n, s) = list(map(int, input().split()))
last = [0 for i in range(s + 1)]
for i in range(n):
    (f, t) = list(map(int, input().split()))
    last[f] = max(last[f], t)
ans = -1
for i in range(s, -1, -1):
    ans += 1
    ans = max(ans, last[i])
print(ans)
