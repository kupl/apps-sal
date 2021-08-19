n = input()
fx = 0
for i in n:
    fx += int(i)
if int(n) % fx == 0:
    print('Yes')
else:
    print('No')
