n, p = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))
a.sort()
result = []
for x in range(a[-1]):
    fail = 0
    for i in range(len(a) - 1, -1, -1):
        if (x + i) < a[i]:
            fail = 1
            break
        elif p <= min(i + 1, i - (a[i] - x - 1)):
            fail = 1
            break
    if fail == 0:
        result.append(str(x))
print(len(result))
if result:
    print(' '.join(result))
