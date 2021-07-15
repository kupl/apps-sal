n = int(input())
left = []
right = []
for i in range(n):
    tmp = tuple(map(int, input().split()))
    if tmp[0] < 0:
        left.append(tmp)
    else:
        right.append(tmp)
m = len(left) - len(right)
all1 = left + right
ans = 0
if m == 1 or m == -1 or m == 0:
    for i in range(n):
        ans += all1[i][1]
    print(ans)
    return
if m < 0:
    all1.sort()
    for i in range(len(left) * 2 + 1):
        ans += all1[i][1]
    print(ans)
    return
all1.sort()
for i in range(m - 1, n):
    ans += all1[i][1]
print(ans)

