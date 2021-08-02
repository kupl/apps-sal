n = str(input())
num = 0
for i in range(len(n)):
    num += int(n[i])
if int(n) % num == 0:
    print('Yes')
else:
    print('No')
