n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
criteria = sum(a) / (m * 4)

ans = 0
for i in a:
    if i >= criteria:
        ans += 1

if ans >= m:
    print('Yes')
else:
    print('No')
