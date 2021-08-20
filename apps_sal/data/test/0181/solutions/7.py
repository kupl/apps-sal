n = int(input())
n = n * -1 % 360
minVueltas = -1
minValor = -1
for i in range(4):
    temp = (n + 90 * i) % 360
    if temp > 180:
        temp = 360 - temp
    if minValor == -1 or temp < minValor:
        minVueltas = i
        minValor = temp
print(minVueltas)
