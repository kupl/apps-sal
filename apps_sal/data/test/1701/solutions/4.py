(n, m) = list(map(int, input().strip().split(' ')))
ips = {}
for _ in range(n):
    (name, ip) = input().strip().split(' ')
    ips[ip] = name
for _ in range(m):
    line = input().strip().split(' ')
    line[1] = line[1] + ' ' + '#' + ips[line[1][:-1]]
    print(' '.join(line))
