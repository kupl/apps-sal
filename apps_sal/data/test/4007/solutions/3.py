n = int(input())
mas = list(map(int, input().split()))
cou = []
for i in range(n + 1):
    cou.append(0)
x = -1
for i in range(n):
    if mas[i] == 0:
        if x == -1:
            x = i
        else:
            y = i
for i in range(n):
    cou[mas[i]] = 1
num = n
for i in range(1, n + 1):
    if cou[i] != 1:
        cou[i] = 1
        while True:
            num -= 1
            if mas[num] == 0:
                mas[num] = i
                break
for i in range(n):
    if mas[i] == i + 1:
        if i == x:
            mas[i], mas[y] = mas[y], mas[i]
        else:
            mas[i], mas[x] = mas[x], mas[i]
print(*mas)
