a,b = map(int,input().split())
sa = set()
sb = set()
i = 1
while i * i <= max(a,b):
    if a % i == 0:
        sa.add(i)
        sa.add(a//i)
    if b % i == 0:
        sb.add(i)
        sb.add(b//i)
    i += 1
s = sa & sb
s.remove(1)
for x in list(s):
    for y in list(s):
        if x == y:
            continue
        if y % x == 0:
            s.remove(y)
print(len(s) + 1)
