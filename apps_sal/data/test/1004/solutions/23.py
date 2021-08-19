n = int(input())
a = list(map(int, input().split()))
s = set()
d = 0
ans = []
c = 0
o = set()
for i in range(n):
    x = a[i]
    if x > 0:
        if i == 0:
            c += 1
            s.add(x)
            o.add(x)
        elif len(s):
            if x in s or x in o:
                d = -1
                break
            else:
                c += 1
                s.add(x)
                o.add(x)
        else:
            d += 1
            ans.append(c)
            s.add(x)
            o = {x}
            c = 1
    elif x < 0:
        if i == 0:
            d = -1
            break
        elif len(s):
            if -1 * x in s:
                s.remove(-1 * x)
                c += 1
            else:
                d = -1
                break
        else:
            d = -1
            break
if d != -1:
    if len(s):
        print('-1')
    else:
        d += 1
        ans.append(c)
        print(d)
        print(*ans)
else:
    print('-1')
