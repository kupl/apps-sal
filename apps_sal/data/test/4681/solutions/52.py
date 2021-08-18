
n = int(input())

luca = [2, 1]

if n >= 2:
    for i in range(n - 1):
        luca.append(luca[-1] + luca[-2])
    print(luca[-1])

else:
    print(1)
