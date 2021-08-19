(a, b) = tuple(map(int, input().split()))
ans = [0] * 3
for i in range(1, 7, 1):
    if abs(i - a) < abs(i - b):
        ans[0] += 1
    elif abs(i - a) > abs(i - b):
        ans[2] += 1
    else:
        ans[1] += 1
print(' '.join(map(str, ans)))
