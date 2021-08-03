from collections import deque
s = str(input())
q = int(input())
stat = 0
l = []
a = deque()
b = deque()
for i in range(q):
    l = list(map(str, input().split()))
    t = int(l[0])
    if t == 1:
        stat += 1
    else:
        f = int(l[1])
        c = l[2]
        if stat % 2 == 0:
            if f == 1:
                a.appendleft(c)
            else:
                b.append(c)
        else:
            if f == 1:
                b.append(c)
            else:
                a.appendleft(c)

#print(a, b, stat % 2)
ans = ''.join(a) + s + ''.join(b)
if stat % 2 == 1:
    ans = ans[::-1]
print(ans)
