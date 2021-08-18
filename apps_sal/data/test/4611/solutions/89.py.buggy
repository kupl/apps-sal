n = int(input())
arr = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    t1, x1, y1 = arr[i]
    t2, x2, y2 = arr[i + 1]
    if abs(x1 - x2) + abs(y1 - y2) > t2 - t1:
        print('No')
        return
    if (abs(x1 - x2) + abs(y1 - y2)) % 2 != (t2 - t1) % 2:
        print('No')
        return
print('Yes')
