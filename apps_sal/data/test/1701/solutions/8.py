(n, m) = map(int, input().split())
d = {}
for i in range(n):
    (name, ip) = input().split()
    d[ip + ';'] = name
for i in range(m):
    (command, ip) = input().split()
    print('{} {} #{}'.format(command, ip, d[ip]))
