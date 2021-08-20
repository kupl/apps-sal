(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * n
b = sorted(a, reverse=True)
c = sum(a)
if b[m - 1] >= c / (4 * m):
    print('Yes')
else:
    print('No')
