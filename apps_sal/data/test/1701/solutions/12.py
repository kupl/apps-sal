n, m = list(map(int, input().split()))
d = {}
for i in range(n):
    name, ip = input().split()
    d[ip] = name

for i in range(m):
    comm, ip = input().split()
    name = d[ip[:-1]]
    print(comm+" "+ip+" #"+name)

