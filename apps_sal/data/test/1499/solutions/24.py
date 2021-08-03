n, m = list(map(int, input().split()))
left = []
right = []
for i in range(n):
    left.append([])
    right.append([])
for i in range(m):
    if i < 2 * n:
        if i % 2 == 0:
            left[i // 2].append(i + 1)
        else:
            right[i // 2].append(i + 1)
    else:
        if i % 2 == 0:
            left[(i - 2 * n) // 2].append(i + 1)
        else:
            right[(i - 2 * n) // 2].append(i + 1)


s = ''
for i in range(n):
    for j in range(len(left[i]) - 1, -1, -1):
        s += str(left[i][j]) + ' '
    for j in range(len(right[i]) - 1, -1, -1):
        s += str(right[i][j]) + ' '
print(s[:-1])
