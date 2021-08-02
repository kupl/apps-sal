input()
a = list(map(int, input().split()))
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(sum([j if i > j else j - i for i, j in d.items()]))
