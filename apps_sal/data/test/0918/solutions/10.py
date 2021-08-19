(n, m) = list(map(int, input().split()))
b = [[0] * 3 for i in range(n)]
for i in range(n):
    (b[i][2], b[i][0], b[i][1]) = list(map(str, input().split()))
    b[i][0] = int(b[i][0])
    b[i][1] = int(b[i][1])
b.sort()
j = 0
for i in range(m):
    k = 0
    while j < n and b[j][0] == i + 1:
        k += 1
        j += 1
    if k > 2 and b[j - 2][1] == b[j - 3][1]:
        print('?')
    elif k > 0:
        print(b[j - 1][2] + ' ' + b[j - 2][2])
