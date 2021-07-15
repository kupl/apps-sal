n = int(input())
if n <= 2:
    print(-1)
else:
    x = ''
    for i in range(n,0,-1):
        x += str(i) + ' '
    print(x[:-1])

