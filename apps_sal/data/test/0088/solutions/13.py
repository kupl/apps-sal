(low, high) = [int(x) for x in input().split()]
a = 2
x = 0
tot = 0
while True:
    for b in reversed(list(range(a - 1))):
        x = 2 ** a - 1 - 2 ** b
        if x < low:
            continue
        if x > high:
            break
        tot += 1
    if x > high:
        break
    a += 1
print(tot)
