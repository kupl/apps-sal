N = int(input())
A = list(map(int, input().split()))
di = {}
for a in A:
    if a not in di.keys():
        di[a] = 1
    else:
        di[a] += 1
sum = 0
for (a, b) in di.items():
    sum += int(b * (b - 1) / 2 * 1)
for k in A:
    n = di[k]
    bef = n * (n - 1) / 2
    aft = (n - 1) * (n - 2) / 2
    print(int(sum - bef + aft))
