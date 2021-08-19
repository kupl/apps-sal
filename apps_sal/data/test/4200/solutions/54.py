(n, m) = map(int, input().split())
a = list(map(int, input().split()))
ans = [i for i in a if i >= sum(a) / 4 / m]
if len(ans) >= m:
    print('Yes')
else:
    print('No')
