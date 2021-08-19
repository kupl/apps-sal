from sys import stdin, stdout
(n, a, m, b) = (int(stdin.readline()), sorted(list(map(int, stdin.readline().split())), reverse=True), int(stdin.readline()), list(map(int, stdin.readline().split())))
s = sum(a)
for i in range(m):
    print(s - a[b[i] - 1])
