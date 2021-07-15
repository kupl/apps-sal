n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input())
for i in range(n):
    for j in range(m):
        if a[i][j] is '.':
            print('W' if (i + j) % 2 else 'B', end = '')
        else:
            print('-', end = '')
    print()
