(n, m) = list(map(int, input().split(' ')))
iptable = {}
for i in range(n):
    (a, b) = input().split(' ')
    iptable[b] = a
for i in range(m):
    (a, b) = input().split(' ')
    print(a, b, '#' + iptable[b[:-1]])
