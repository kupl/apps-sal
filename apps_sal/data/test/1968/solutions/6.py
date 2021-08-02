
n, v = [int(i) for i in input().split()]
yes = []
for i in range(n):
    l = [int(i) for i in input().split()]
    for j in l[1:]:
        if v > j:
            yes += [i + 1]
            break

print(len(yes))
for i in yes:
    print(i, end=' ')
