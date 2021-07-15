s = list(input())
t = list(input())
n = len(s)
m = len(t)
k = -1
for i in range(n-m+1):
    x = s[i:i+m]
    flg = True
    for j in range(m):
        if x[j] != '?' and x[j] != t[j]:
            flg = False
            break
    if flg:
        k = i
if k != -1:
    for i in range(k,k+m):
        s[i] = t[i-k]
    for i in range(n):
        if s[i] == '?':
            s[i] = 'a'
    print(''.join(s))
else:
    print('UNRESTORABLE')
