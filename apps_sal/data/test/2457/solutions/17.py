t = int(input())
for i in range(t):
    (n, a, b, c, d) = map(int, input().split())
    flag = 0
    if n * (a - b) > c + d or n * (a + b) < c - d:
        flag = 1
    if flag == 0:
        print('Yes')
    else:
        print('No')
