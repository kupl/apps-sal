n_1 = int(input())
sn = 0
n = n_1
while n > 0:
    sn += n % 10
    n //= 10
if n_1 % sn == 0:
    print('Yes')
else:
    print('No')
