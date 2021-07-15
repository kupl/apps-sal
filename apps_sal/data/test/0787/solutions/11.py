import sys


n = int(input())
s = str(input())
l = []

for i in s:
    if not i in l:
        l.append(i)

vals = []

if len(l) < n:
    print("NO")
    return
else:
    print("YES")
    for i in range(n):
        vals.append(s.index(l[i]))

for i in range(n):
    if i == n-1:
        print(s[vals[len(vals)-1]:len(s)])
    else:
        print(s[vals[i]:vals[i+1]])

