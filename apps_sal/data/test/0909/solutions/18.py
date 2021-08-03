num = []
num.append(int(input()))
num.append(int(input()))
num.append(int(input()))
while(min(num) == 1):
    m = num.index(1)
    num.pop(m)
    if m >= len(num):
        num[m - 1] += 1
    elif m == 0:
        num[m] += 1
    elif num[m - 1] < num[m]:
        num[m - 1] += 1
    else:
        num[m] += 1
m = 1
for i in range(len(num)):
    m *= num[i]
print(m)
