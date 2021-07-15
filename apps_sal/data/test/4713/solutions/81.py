N = int(input())
S = input()

x = 0
x_max = x

for c in S:
    if c == "I":
        x += 1
        if x > x_max:
            x_max = x
    elif c == "D":
        x -= 1

print(x_max)
