n = int(input())
h = list(map(int, input().split()))
if n == 1:
    print('Yes')
    return
res = h[n - 1]
for i in range(1, n):
    if h[n - 1 - i] - res <= 1:
        res = min(res, h[n - 1 - i])
    else:
        print('No')
        return
print('Yes')
