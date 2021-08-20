(a, b) = map(int, input().split())
tap = 0
outlet = 1
while outlet < b:
    outlet -= 1
    outlet += a
    tap += 1
print(tap)
