a, b, f, k = [int(i) for i in input().split(" ")]
x = f
y = a - f
oil = b
result = 0
alert = 0


if k == 1:
    oil -= x
    if oil < 0:
        alert = 1
    if oil < y:
        result += 1
        oil = b
    oil -= y
    if oil < 0:
        alert = 1
else:
    oil -= x
    if oil < 0:
        alert = 1
    if oil < 2 * y:
        result += 1
        oil = b

    if k == 2:
        oil -= 2 * y
        if oil < 0:
            alert = 1
        if oil < x:
            result += 1
            oil = b
    else:
        oil -= 2 * y
        if oil < 0:
            alert = 1
        if oil < 2 * x:
            result += 1
            oil = b

if k > 2:
    k -= 2
    for ii in range(int((k - 1) / 2)):
        oil -= 2 * x
        if oil < 0:
            alert = 1

        if oil < 2 * y:
            oil = b
            result += 1
        k -= 1
        oil -= 2 * y
        if oil < 0:
            alert = 1
        if oil < 2 * x:
            oil = b
            result += 1
        k -= 1
    if k == 1:
        oil -= 2 * x
        if oil < 0:
            alert = 1
        if oil < y:
            oil = b
            result += 1
    if k == 2:
        oil -= 2 * x
        if oil < 0:
            alert = 1
        if oil < 2 * y:
            oil = b
            result += 1
        oil -= 2 * y
        if oil < x:
            oil = b
            result += 1
if alert == 1:
    print(-1)
else:
    print(result)
