a, b, c, d = map(int, input().split(' '))
x = int(max(3 * a / 10, a - a * c / 250))
y = int(max(3 * b / 10, b - b * d / 250))

if x == y:
    print("Tie")
if x < y:
    print("Vasya")
if x > y:
    print("Misha")
