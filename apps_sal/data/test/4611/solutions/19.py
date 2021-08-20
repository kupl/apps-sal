N = int(input())
res = True
(pre_t, pre_x, pre_y) = (0, 0, 0)
for _ in range(N):
    (t, x, y) = list(map(int, input().split()))
    tmp = t - pre_t - abs(x - pre_x) - abs(y - pre_y)
    if tmp < 0 or tmp % 2 == 1:
        res = False
        break
    pre_t = t
    pre_x = x
    pre_y = y
print('Yes' if res else 'No')
