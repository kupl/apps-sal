

num, sdollars = input().split(' ')
n = int(num)
s = int(sdollars)
sweets = -1

for i in range(0, n):

    dollars, cents = input().split(' ')
    d = int(dollars)
    c = int(cents)

    if s < d:
        continue

    if s == d and c > 0:
        continue

    if c == 0:
        if (sweets == -1):
            sweets = 0
        continue

    if (100 - c) > sweets:
        sweets = 100 - c

print(sweets)
