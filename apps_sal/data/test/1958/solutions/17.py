n, p = list(map(int, input().split()))
s = []
for i in range(n):
    s.append(input().strip())
cnt = 0
ans = 0
for c in reversed(s):
    ans += p * cnt
    cnt *= 2
    if c == 'halfplus':
        cnt += 1
        ans += p // 2
print(ans)
