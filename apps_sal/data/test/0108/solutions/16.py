s = input()
k = 0
n = 97
a = []
for i in s:
    a.append(i)
for i in range(len(s)):
    if ord(a[i]) <= n:
        a[i] = chr(n)
        n+=1
        k+=1
    if k == 26:
        break
if k < 26:
    print(-1)
else:
    print(*a,sep = '')
