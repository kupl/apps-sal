a, b, f, k = list(map(int, input().split()))
# if 2*f > b or 2*(a - f) > b:
#     print(-1)
#     return
fuel_count = 0
fuel = b
i = 0
fuel -= f
if fuel < 0:
    print(-1)
    return
while True:
    if fuel >= a - f and i + 1 == k:
        break
    if b >= a - f and i + 1 == k:
        fuel_count += 1
        break
    elif fuel < 2*(a - f):
        fuel = b
        fuel_count += 1
        if fuel < 2*(a - f):
            print(-1)
            return
    fuel -= 2*(a - f)
    i += 1
    if i == k:
        break
    if fuel >= f and i + 1 == k:
        break
    if b >= f and i + 1 == k:
        fuel_count += 1
        break
    elif fuel < 2*f:
        fuel = b
        fuel_count += 1
        if fuel < 2*f:
            print(-1)
            return
    fuel -= 2*f
    i += 1
    if i == k:
        break
print(fuel_count)


