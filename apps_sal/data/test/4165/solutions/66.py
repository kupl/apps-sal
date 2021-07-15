
N = list(map(int,input().split()))
side = list(map(int, input().split()))
long_side = max(side)
total = 0
for i in side:
    total += i

total -= long_side

if long_side < total:
    print('Yes')
else:
    print('No')

