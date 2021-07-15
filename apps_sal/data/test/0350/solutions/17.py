n = int(input())
a = [int(x) for x in input().split()]

occ = set()
a.sort(reverse=True)
for i in range(len(a)):
    while a[i] in occ and a[i] > 0:
        a[i] -= 1
    occ.add(a[i])

print(sum(a))

