i = int(input())
s = input().split()
m = max (list(map(int,s)))
l = []
for j in s:
    if not l or  int(j) < l[-1] :
        l.append(int(j))
    elif int(j) == l[-1]:
        l.pop()
    else:
        print('NO')
        return

if (len(l) ==1 and l[0] >= m) or len(l) == 0 :
    print('YES')
else:
    print('NO')

