test = int(input())
for ii in range(test):
    (a, b, n, m) = list(map(int, input().split()))
    if a + b < m + n:
        print('No')
        continue
    if a > b:
        (a, b) = (b, a)
    if a < m:
        print('No')
        continue
    rem = a - m
    if b + rem < n:
        print('No')
        continue
    print('Yes')
