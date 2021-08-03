N = input()
x = 0
for i in range(len(N)):
    x += int(N[i])
if int(N) % x == 0:
    print('Yes')
else:
    print('No')
