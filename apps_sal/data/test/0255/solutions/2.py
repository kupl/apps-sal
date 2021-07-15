n = int(input())
ns = sorted(map(int, str.split(input())))
m = int(input())
ms = sorted(map(int, str.split(input())))
ni = mi = pairs = 0
while ni < n and mi < m:

    if abs(ns[ni] - ms[mi]) <= 1:

        pairs += 1
        ni += 1
        mi += 1

    elif ns[ni] <= ms[mi]:

        ni += 1

    else:

        mi += 1

print(pairs)

