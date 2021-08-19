n = str(input())
sum = 0
for i in range(0, len(n)):
    sum += int(n[i])
if int(n) % sum == 0:
    print('Yes')
else:
    print('No')
