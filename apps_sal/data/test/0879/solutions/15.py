n = int(input())
p = list(map(int, input().split()))
o = []
c = n
while c!=1:
    o.append(c)
    c = p[c-2]
o.append(1)
o = reversed(o)
print(*o)

