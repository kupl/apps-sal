n = int(input().strip())
a = sorted(list(map(int, input().strip().split())))
r = 0

while True:
    mean = sum(a) / n
    if round(mean) >= 5 or mean == 4.5:
        break

    r += 1
    a[0] = 5
    a.sort()

print(r)
