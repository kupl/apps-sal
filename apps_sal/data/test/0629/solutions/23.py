n = int(input())
up = [int(item) for item in input().split()]
down = [int(item) for item in input().split()]
j = [int(item) for item in input().split()]
time = 0
mas = []
for idx in range(n - 1, -1, -1):
    mas.append(j[idx] + sum([n for n in up[0:idx]]) + sum([n for n in down[idx:]]))
mas.sort()
print(mas[0] + mas[1])
