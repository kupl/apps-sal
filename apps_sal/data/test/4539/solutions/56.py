n = str(input())
sum = 0
for i in range(len(n)):
    sum = sum + int(n[i])
if int(n) % sum == 0:
    print('Yes')
else:
    print('No')
