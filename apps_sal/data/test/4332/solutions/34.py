N = input()
Sn = 0
for i in range(len(N)):
    Sn += int(N[i])
if int(N) % Sn == 0:
    print('Yes')
else:
    print('No')
