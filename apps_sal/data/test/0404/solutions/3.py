b = int(input())
divs = 0
i = 1
while i <= b ** 0.5:
    if i == b ** 0.5:
        divs += 1
    elif b % i == 0:
        divs += 2
    i += 1
print(divs)
