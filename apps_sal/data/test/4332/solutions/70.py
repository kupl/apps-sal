n = int(input())
n_ = n
sn = 0
while n_ != 0:
    sn += n_ % 10
    n_ = n_ // 10
if n % sn == 0:
    print('Yes')
else:
    print('No')
