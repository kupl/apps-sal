s = list(input())
t = list(input())

ss = len(s)
tt = len(t)

ans = tt
for i in range(ss - tt + 1):

    u = s[i:i + tt]
    cnt = 0
    for j in range(tt):
        if u[j] == t[j]:
            cnt += 1
            ans_ = tt - cnt
            ans = min(ans, ans_)
print(ans)
