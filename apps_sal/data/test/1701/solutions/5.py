n,m = list(map(int,input().split()))

D = {}
for _ in range(n):
    name,ip = input().split()
    D[ip] = name

for _ in range(m):
    s = input()
    ip = s.split()[1][:-1]
    s += ' #'+D[ip]
    print(s)

