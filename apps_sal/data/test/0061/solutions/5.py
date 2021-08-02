a = []
for i in range(2):
    n, b = list(map(int, input().split()))
    a.append(0)
    for x in map(int, input().split()):
        a[-1] = a[-1] * b + x
print('<>='[(a[0] == a[1]) + (a[0] >= a[1])])
