n = int(input())
a = list(map(int, input().split()))
perms = []
for i in range(n):
    min_i = min(list(range(i, n)), key=lambda x: a[x])

    if min_i != i:
        perms.append([i, min_i])
        a[i], a[min_i] = a[min_i], a[i]

print(len(perms))
for p1, p2 in perms:
    print(p1, p2)
