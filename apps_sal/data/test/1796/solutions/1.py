line = int(input())
x = 0

for i in range(0, line):
    a = input()

    if '+' in a:
        x += 1

    elif '-' in a:
        x -= 1

print(x)
