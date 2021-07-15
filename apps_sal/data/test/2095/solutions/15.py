cars = []
for i in range(int(input())):

    a = 0
    for x in map(int, str.split(input())):

        if x > 0:

            a |= x

    if a & 1 == 0:

        cars.append(i + 1)

print(len(cars))
if cars:

    print(str.join(" ", list(map(str, cars))))

