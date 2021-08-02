n = int(input())
a = [[] for i in range(110)]
for i in range(n):
    x = input()
    a[len(x)].append(x)
l = []
for i in a:
    for j in i:
        l.append(j)
x = l[0]
f = 1
# print(a,l)
for i in range(1, n):
    if(l[i].find(x) == -1):
        f = 0
    x = l[i]
if(f):
    print('YES')
    for i in l:
        print(i)
else:
    print('NO')
