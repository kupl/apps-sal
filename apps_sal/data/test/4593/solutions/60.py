x = int(input())
ex = [0 for i in range(1001)]
ex[1] = 1

for i in range(2, 1001):
    tmp = i * i
    while tmp <= 1000:
        ex[tmp] = 1
        tmp *= i

for i in range(x, 0, -1):
    if ex[i] == 1:
        print(i)
        break
