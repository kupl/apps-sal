(n, m) = map(int, input().split())
a = list(map(int, input().split()))
aa = sum(a)
count = 0
for i in range(len(a)):
    if a[i] >= aa * (1 / (4 * m)):
        count += 1
    else:
        pass
if count >= m:
    print('Yes')
else:
    print('No')
