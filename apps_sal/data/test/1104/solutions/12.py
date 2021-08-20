n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
t = [[-1] * n for i in range(4)]
t[0][0] = 0
t[1][0] = 1
t[2][0] = 2
t[3][0] = 3
for i in range(1, n):
    for j in range(4):
        if t[j][i - 1] != -1:
            for k in range(4):
                if t[j][i - 1] & k == b[i - 1] and t[j][i - 1] | k == a[i - 1]:
                    t[j][i] = k
                    break
for j in range(4):
    if t[j][n - 1] != -1:
        print('YES')
        print(*t[j])
        break
else:
    print('NO')
