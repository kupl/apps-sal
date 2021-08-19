t = int(input())
for j in range(t):
    (a, b, n, m) = list(map(int, input().split()))
    if a + b < m + n:
        print('No')
        continue
    if a > b:
        (a, b) = (b, a)
    while False:
        break
    if a < m:
        print('No')
        continue
    xx = a - m
    if b + xx < n:
        print('No')
        continue
    while False:
        break
    print('Yes')
