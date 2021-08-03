n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
k = sum(a) * (1 / (4 * m))
b = [i for i in a if i >= k]

if len(b) >= m:
    print('Yes')
else:
    print('No')
