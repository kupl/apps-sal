n = list(input())
num = 0
for i in range(len(n)):
    num += int(n[i])
if num % 9 == 0:
    print('Yes')
else:
    print('No')
