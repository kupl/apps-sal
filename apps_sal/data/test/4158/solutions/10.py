n = int(input())
a = [int(s) for s in input().split(' ')]
best_m = 1
best_res = []
best_res.append(a[0])
powers = []
for i in range(31):
    powers.append(2 ** i)
s = set()
for i in range(n):
    s.add(a[i])
for i in range(n):
    if best_m == 3:
        break
    x = a[i]
    for p in range(31):
        d = powers[p]
        if x - d in s and x + d in s:
            best_m = 3
            best_res = [x - d, x, x + d]
            break
        if best_m >= 2:
            continue
        if x - d in s:
            best_m = 2
            best_res = [x - d, x]
            continue
        if x + d in s:
            best_m = 2
            best_res = [x, x + d]
            continue
print(best_m)
print(' '.join([str(x) for x in best_res]))
