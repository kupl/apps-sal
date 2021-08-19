def operate(a, b):
    if a > b:
        if (a - b) % b:
            return (a - b) // b
        else:
            return (a - b) // b + 1
    if b > a:
        if (b - a) % a:
            return (b - a) // a
        else:
            return (b - a) // a + 1


for x in range(int(input())):
    (a, b) = [int(x) for x in input().split()]
    count = 0
    while a != 0 and b != 0:
        if a > b:
            factor = (a - b) // b + 1
            a -= factor * b
            count += factor
        else:
            factor = (b - a) // a + 1
            b -= factor * a
            count += factor
    print(count)
