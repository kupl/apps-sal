x = input()
fx = 0
intx = int(x)
for i in range(len(x)):
    fx += int(x[i])
if intx % fx == 0:
    print('Yes')
else:
    print('No')
