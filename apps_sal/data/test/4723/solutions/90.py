s = list(input())
t = list(input())
s.reverse()
t.reverse()
l = len(t)
ld = len(s) - len(t) + 1
for i in range(ld):
    cnt = 0
    for j in range(l):
        if s[j + i] == '?' or s[j + i] == t[j]:
            cnt += 1
    if cnt == l:
        ans = []
        for p in range(i):
            if s[p] == '?':
                ans.append('a')
            else:
                ans.append(s[p])
        for p in t:
            ans.append(p)
        for p in range(ld - i - 1):
            if s[l + p + i] == '?':
                ans.append('a')
            else:
                ans.append(s[l + i + p])
        ans.reverse()
        for p in ans:
            print(p, end='')
        break
else:
    print('UNRESTORABLE')
