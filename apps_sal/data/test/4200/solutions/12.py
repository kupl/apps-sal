(n, m) = map(int, input().split())
li = list(map(int, input().split()))
border = 4 * m
popular = 0
for i in range(len(li)):
    if li[i] < sum(li) * (1 / border):
        continue
    popular += 1
if popular >= m:
    print('Yes')
else:
    print('No')
