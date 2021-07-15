n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

diff = []
for i in range(n):
    if a[i] != b[i]:
        diff.append(i)
sa = True
sb = True
di = []
for i in range(1,n+1):
    di.append(i)
s = []
for i in range(n):
    if i not in diff:
        s.append(a[i])
        di.remove(a[i])
    else:
        s.append(0)
if len(diff) == 1:
    s[diff[0]] = di[0]
else:
    if (a[diff[0]] in di and b[diff[1]] in di):
        s[diff[0]] = a[diff[0]]
        s[diff[1]] = b[diff[1]]
    else:
        s[diff[0]] = b[diff[0]]
        s[diff[1]] = a[diff[1]]
        
        

for i in range(n):
    print(s[i], end= ' ')


