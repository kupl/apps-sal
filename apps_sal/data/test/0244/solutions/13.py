n = int(input())
x = int(input())

n %= 6

odd = n % 2

for i in range(n):
    if odd:
        if x == 0:
            x = 1
        elif x == 1:
            x = 0
    else:
        if x == 1:
            x = 2
        elif x == 2:
            x = 1
    odd = not odd

print(x)

