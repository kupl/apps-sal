s = input()
t = input()
n = len(s)
m = len(t)
ans = []
for i in range(n-m+1):
    c = 0
    for j in range(m):
        if s[i+j] == '?' or s[i+j] == t[j]:
            c += 1
    if c == m:
        s_ = s[0:i] + t + s[i+m:]
        s_ = s_.replace('?', 'a')
        ans.append(s_)
if len(ans)>0:
    print((sorted(ans)[0]))
else:
    print('UNRESTORABLE')

