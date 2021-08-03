with open(0) as f:
    N, *a = list(map(int, f.read().split()))
i, j, k = 0, 0, 0
for x in a:
    if x % 4 == 0:
        i += 1
    elif x % 2 == 0:
        j += 1
    else:
        k += 1

if j > 0:
    k += 1
print(('Yes' if k <= i + 1 else 'No'))
