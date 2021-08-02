N = input()

tmp = 0
for i in range(len(N)):
    tmp += int(N[i])
if int(N) % tmp == 0:
    print('Yes')
else:
    print('No')
