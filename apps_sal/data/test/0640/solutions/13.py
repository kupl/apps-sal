(a, b) = [int(s) for s in input().split()]
ans = [0, 0, 0]
for i in range(1, 7):
    if abs(a - i) < abs(b - i):
        ans[0] += 1
    elif abs(a - i) == abs(b - i):
        ans[1] += 1
    else:
        ans[2] += 1
print(*ans)
