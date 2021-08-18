n, m = list(map(int, input().split()))
ip = {}
for i in range(n):
    a, b = input().split()
    ip[b] = a
for i in range(m):
    a, b = input().split()
    print(a, b + '
