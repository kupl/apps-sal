s = input()
t = input()
ans = ''

# for i in range(len(s)-len(t)+1):
for i in range(len(s)-len(t), -1, -1):
    st = s[i:i+len(t)]
    cnt = 0
    for si, ti in zip(st, t):
        if si == '?' or si == ti:
            cnt += 1
        # print(si, ti, cnt)
    if cnt == len(t):
        ans = s[:i] + t + s[i+len(t):]
        ans = ans.replace('?', 'a')
        print(ans)
        return
else:
    print('UNRESTORABLE')



