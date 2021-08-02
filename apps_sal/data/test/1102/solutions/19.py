n, a = (int(i) for i in input().split())
l = list(map(int, input().split()))
a -= 1
ans = 0
for d in range(n):
    if d == 0 and l[a] == 1:
        ans += 1
    elif a - d >= 0 and a + d < n and l[a - d] == 1 and l[a + d] == 1:
        ans += 2
    elif a - d < 0 and a + d < n and l[a + d] == 1:
        ans += 1
    elif a - d >= 0 and a + d >= n and l[a - d] == 1:
        ans += 1

print(ans)
