n = int(input().strip())
p = [int(x) for x in input().split()]

l = {}
for x in p:
    if x - 1 in l:
        l[x] = l[x - 1] + 1
    else:
        l[x] = 1

print(n - max(l.values()))
