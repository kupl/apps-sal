s = input()
t = input()
lt = len(t)
ans = []
for i in range(len(s)-lt+1):
    cnt = 0
    n = 0
    while n < lt:
        if s[i+n] == '?':
            cnt += 1
        else:
            if s[i+n] == t[n]:
                cnt += 1
        n += 1
    if cnt == lt:
        ans.append(list(s[:i] + t + s[i+lt:]))
        # print(ans)
        # break

if len(ans) != 0:
    for a in ans:
        # print(a)
        for i in range(len(a)):
            if a[i] == '?':
                a[i] = 'a'
    ans.sort()
    print(*ans[0], sep='')

else:
    print('UNRESTORABLE')
