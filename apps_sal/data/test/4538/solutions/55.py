num, max_num = list(map(int, input().split()))
x = []
y = []
count = 0

for i in range(num):
    x1, y1 = list(map(int, input().split()))
    x.append(x1)
    y.append(y1)

for i in range(len(x)):
    temp = (x[i]**2 + y[i]**2)**(1 / 2)
    if temp <= max_num:
        count += 1

print(count)
