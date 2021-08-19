(a, m) = list(map(int, input().split()))
while m % 2 == 0:
    m = m // 2
if a % m == 0:
    print('Yes')
else:
    print('No')
