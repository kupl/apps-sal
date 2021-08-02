n, m = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]
f = [int(x) for x in input().split()]
l = []
for x in s:
    if x in f:
        l.append(str(x))
print(" ".join(l))
