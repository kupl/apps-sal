n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))
left = 0
right = 10 ** 9
while right - left > 1e-07:
    mid = (left + right) / 2
    a = min(x)
    b = max(x)
    for i in range(n):
        a = max(a, x[i] - v[i] * mid)
        b = min(b, x[i] + v[i] * mid)
    if a > b:
        left = mid
    else:
        right = mid
print('%.7f' % right)
