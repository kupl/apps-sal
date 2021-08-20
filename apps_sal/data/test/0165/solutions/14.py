l = list(map(int, input().split()))
l = sorted(l, reverse=True)
min_result = 10000000000000000000000000000
delts = [(1, 0, 0), (1, 1, 0), (0, 0, 1), (0, 1, 1), (0, 0, 0)]
for delt in delts:
    a = []
    for i in range(3):
        a.append(l[i] + delt[i])
    a = sorted(a, reverse=True)
    min_result = min(min_result, a[0] - a[1] + a[0] - a[2])
print(min_result)
