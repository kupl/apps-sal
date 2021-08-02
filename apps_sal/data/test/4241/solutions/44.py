s = input()
t = input()
sl = len(s)
tl = len(t)
ans = 10**9
for i in range(sl - tl + 1):
    cnt = 0
    for j in range(tl):
        if s[i + j] != t[j]:
            cnt += 1
    ans = min(ans, cnt)
print(ans)
