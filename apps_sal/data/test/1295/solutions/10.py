n, m = map(int, input().split())
c = list(map(int, input().split()))
t = list(map(int, input().split()))
i = 0
ans = 0
for x in c:
    while i < m - 1 and abs(x - t[i]) >= abs(x - t[i + 1]):
        i += 1
    ans = max(ans, abs(x - t[i]))
print(ans)
