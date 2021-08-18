n, m = list(map(int, input().split()))
ips = dict()
for _ in range(n):
    s = input().strip().split()
    ips[s[1]] = s[0]
for _ in range(m):
    s = input().strip().split()
    s[1] = s[1][:-1]
    print(s[0], s[1] + ";", "
