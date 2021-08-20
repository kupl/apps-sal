(x, N) = list(map(int, input().split()))
p = list(map(int, input().split()))
min = 10000
temp = 0
num = 10000
for i in range(-1000, 1000):
    temp = abs(x - i)
    if temp < min and i not in p:
        min = temp
        num = i
print(num)
