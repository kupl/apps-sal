from sys import stdin, stdout
t = int(stdin.readline())
for i in range(t):
    (n, m) = list(map(int, stdin.readline().split()))
    arr = list(map(int, stdin.readline().split()))
    if sum(arr) == m:
        print('YES')
    else:
        print('NO')
