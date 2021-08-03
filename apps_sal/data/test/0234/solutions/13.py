def bad_num(k):
    tb = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if pole[i + x][j + y] == '*':
                tb += 1
    return tb == k


n, m = list(map(int, input().split()))
pole = []
for i in range(n):
    arr = list(input().strip())
    arr.append('.')
    pole.append(arr)
pole.append('.' * (m + 1))

for i in range(n):
    for j in range(m):
        cur = pole[i][j]
        if cur == '.':
            cur = '0'
        if cur in '0123456789':
            if bad_num(int(cur)):
                continue
            else:
                print('NO')
                return
        elif cur != '*':
            print('NO')
            return

print('YES')
