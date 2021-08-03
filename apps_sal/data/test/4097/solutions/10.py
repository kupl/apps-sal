n = int(input())
a = [int(x) for x in input().split()]
var = [0, -1, 1]

result = n + 1

if n <= 2:
    print(0)
    return

for x in var:
    for y in var:
        if result == 0:
            continue

        diffrest = (a[0] + x - (a[n - 1] + y)) % (n - 1)
        diff = -(a[0] + x - (a[n - 1] + y)) // (n - 1)
        if diffrest != 0:
            continue

        change = 0 if x == 0 else 1
        last = a[0] + x
        i = 1
        while i < n and change <= n:
            next = last + diff
            ab = abs(next - a[i])
            if ab == 1:
                change += 1
            elif ab > 1:
                change = n + 1
            last = next
            i += 1

        if change < result:
            result = change

print(result if result <= n else -1)
