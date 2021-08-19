n, m = list(map(int, input().split()))

server = {}
for i in range(n):
    name, ip = input().split()
    server[ip] = name

for i in range(m):
    cmd, ip = input().split()
    print('%s %s #%s' % (cmd, ip, server[ip[:-1]]))
