from itertools import permutations
n = int(input())
a = []
for i in range(n):
    a.append(list(input().split()))
pa = list(permutations(a))
for x in range(1, 1000):
    ds = str(x)
    for a in pa:
        for (d, c) in zip(ds, a):
            if d not in c:
                break
        else:
            break
    else:
        break
print(x - 1)
