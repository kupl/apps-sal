# from math import ceil
#from sys import stdout

t = 1  # int(input())
for test in range(1, t + 1):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    arr = [[0 for i in range(m)] for j in range(n)]
    tmp = 0
    for i in a:
        tmp = tmp ^ i
    for i in b:
        tmp = tmp ^ i
    if tmp != 0:
        print("NO")
    else:
        print("YES")
        row = 0
        while row < n - 1:
            arr[row][-1] = a[row]
            b[m - 1] = a[row] ^ b[m - 1]
            row += 1
        for i in range(m):
            arr[n - 1][i] = b[i]

        for i in range(n):
            print(*arr[i])
