iData = list(map(int, str(input()).split(" ")))
n, m = iData[0], iData[1]
a = list(map(int, str(input()).split(" ")))

tmp, bus_count = 0, 1
for i in range(n):
    if tmp + a[i] <= m:
        tmp += a[i]
    else:
        bus_count += 1
        tmp = a[i]

print(bus_count)
