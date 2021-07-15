n,m = list(map(int,input().split()))
g = {}
for i in range(n):
    na,ip = input().split()
    g[ip] = na
for i in range(m):
    a= input()
    c,ip = a.split()
    print(a+' #'+g[ip[:-1]])

