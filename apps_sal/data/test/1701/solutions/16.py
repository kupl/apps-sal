import collections
(n, m) = map(int, input().strip().split(' '))
s = collections.defaultdict(lambda: '')
for i in range(n):
    (server, ip) = input().strip().split(' ')
    s[ip] = server
for i in range(m):
    (cmd, ip) = input().strip().split(' ')
    print(cmd, ip, '#', end='')
    print(s[ip[:-1]])
