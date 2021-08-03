k = int(input())
x, y = list(map(int, input().split()))
if abs(x) + abs(y) == k:
    print((1))
    print((x, y))
    return
cx = cy = cxy = False
if x < 0:
    x = -x
    cx = True
if y < 0:
    y = -y
    cy = True
if x < y:
    x, y = y, x
    cxy = True

if k % 2 == 0 and (x + y) % 2 == 1:
    print((-1))
    return

ans = []
n = max((x + y + k - 1) // k, 2)

if (x + y) % 2 != (n * k) % 2:
    n += 1

if x < k and n == 3:
    mid = (k + x - y) // 2
    ans.append([x, x - k])
    ans.append([x + mid, y - k + mid])
    ans.append([x, y])

else:
    over = (n * k - x - y) // 2
    for i in range(1, n + 1):
        d = i * k
        if d <= y + over:
            ans.append([0, d])
        elif d <= y + over + x:
            ans.append([d - over - y, y + over])
        else:
            ans.append([x, y + (n - i) * k])

if cxy:
    ans = [[i, j] for j, i in ans]
if cx:
    ans = [[-i, j] for i, j in ans]
if cy:
    ans = [[i, -j] for i, j in ans]


print(n)
for i, j in ans:
    print((i, j))
