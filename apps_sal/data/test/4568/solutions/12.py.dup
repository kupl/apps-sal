n = int(input())
s = input()
ans = 0
for i in range(1, n):
    cnt = 0
    l = set(s[:i])
    r = set(s[i:])
    for v in l:
        if v in r:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
