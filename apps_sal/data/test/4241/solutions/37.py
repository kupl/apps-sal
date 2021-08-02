s, t = input(), input()
ls = len(s)
lt = len(t)
ans = 1000000000000
for i in range(ls - lt + 1):
    ans_sub = 0
    for j in range(lt):
        if t[j] != s[i + j]:
            ans_sub += 1
    ans = min(ans, ans_sub)
print(ans)
