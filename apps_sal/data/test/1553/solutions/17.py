n, h = map(int, input().split())
c = list(map(int, input().split()))
i = n
c2 = sorted(c)
if i % 2 == 1:
    s = sum(c2[0:i:2])
else:
    s = sum(c2[1:i:2])
while s > h:
    i -= 1
    c = c[:i]
    c2 = sorted(c)
    if i % 2 == 1:
        s = sum(c2[0:i:2])
    else:
        s = sum(c2[1:i:2])
print(i)
