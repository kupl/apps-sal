n = int(input())
ans = n
s = 0
for i in range(10):
    s += n % 10
    n = n // 10
if ans % s == 0:
    print('Yes')
else:
    print('No')
