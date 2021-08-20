n = input()
x = 0
for i in range(len(n)):
    x += int(n[i])
if int(n) % x == 0:
    print('Yes')
else:
    print('No')
