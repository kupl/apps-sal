n = int(input())
if n < 3:
    print(-1)
else:
    for i in range(n, 0, -1):
        print(i, end=' ')
