n = int(input())
k = 0
tmp = n
while tmp > 0:
    k += tmp % 10
    tmp //= 10
if n % k == 0:
    print('Yes')
else:
    print('No')
