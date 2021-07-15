from sys import stdin

tt = int(stdin.readline())

for loop in range(tt):

    n,m = map(int,stdin.readline().split())
    a = []

    for  i in range(n):
        A = list(map(int,stdin.readline().split()))
        a.append(A)

    for i in range(n):
        for j in range(m):

            if (i+j) % 2 != a[i][j] % 2:
                a[i][j] += 1

    for i in a:
        print (*i)
