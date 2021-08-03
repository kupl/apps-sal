n = int(input())
arr = [['W'] * n for i in range(n)]
for i in range(n):
    for j in range(i % 2, n, 2):
        arr[i][j] = 'B'
for item in arr:
    tot = ''
    for i in item:
        tot += i
    print(tot)
