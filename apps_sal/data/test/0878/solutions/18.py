n = int(input())
a = [int(i) for i in input().split()]

total = 0

suma = dict()
suma[1, 2] = 3
suma[1, 3] = 4
suma[2, 1] = 3
suma[2, 3] = 9999999999999999999999999999999999999999999999999
suma[3, 1] = 4
suma[3, 2] = 9999999999999999999999999999999999999999999999999

for i, j in zip(a[:-1], a[1:]):
    total += suma[i, j]

for i in range(len(a) - 2):
    if a[i] == 3 and a[i + 1] == 1 and a[i + 2] == 2:
        total -= 1

if total < 99999999999999999999999999999:
    print("Finite")
    print(total)
else:
    print("Infinite")
