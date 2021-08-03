n = int(input())
a = [int(i) - 1 for i in input().split()]

m = [-1] * len(a)

# print(m)

scur = set()
snext = set()

scur.add(0)

dist = 0
changed = True
while changed:
    changed = False
    for i in scur:
        if m[i] == -1 or m[i] > dist:
            m[i] = dist
            if i + 1 < n:
                snext.add(i + 1)
            if i - 1 >= 0:
                snext.add(i - 1)
            snext.add(a[i])
            changed = True
    scur = snext
    snext = set()
    dist += 1

for i in m:
    print(i, end=' ')
print()
