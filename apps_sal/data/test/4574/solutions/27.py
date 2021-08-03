n = int(input())
a = list(map(int, input().split()))
a.sort()
l = []
while a:
    x = a.pop()
    if not a:
        break
    if a[-1] == x:
        a.pop()
        l.append(x)
    if len(l) == 2:
        break
if len(l) != 2:
    print(0)
else:
    print(l[0] * l[1])
