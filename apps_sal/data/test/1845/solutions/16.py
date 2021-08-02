n = int(input())
a = [int(t) for t in input().split(' ')]

min_number = min(a)

defaultpower = sum(a)
minpower = defaultpower

for m in range(2, max(a) + 1):
    maxi = -1
    for i in range(n):
        if a[i] % m == 0 and (maxi == -1 or a[i] > a[maxi]):
            maxi = i

    if maxi == -1:
        continue

    power = defaultpower - min_number - a[maxi] + min_number * m + a[maxi] // m

    minpower = min(power, minpower)

print(minpower)
