(n, h) = map(int, input().split())
(al, bl) = ([], [])
for i in range(n):
    (a, b) = map(int, input().split())
    al.append(a)
    bl.append(b)
ma = max(al)
bl.sort()
s = 0
c = 0
for i in bl[::-1]:
    if ma >= i:
        break
    else:
        s += i
        c += 1
        if s >= h:
            break
if h > s:
    c += (h - s - 1) // ma + 1
print(c)
