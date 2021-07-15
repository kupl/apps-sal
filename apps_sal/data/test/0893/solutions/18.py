 
d, n = list(map(int,input().split()))
a = list(map(int, input().split()))

mas = [[] for _ in range(n+1)]

MOD = 1000000007
for _ in range(n-1):
    u, v = list(map(int,input().split()))
    mas[u].append(v)
    mas[v].append(u) 


def dfs(nomer,mas,tyt_yge_bili,f,nach):
    f[nomer] = 1;
    tyt_yge_bili[nomer] = True
    for j in mas[nomer]:
        if tyt_yge_bili[j]!=True:
            if ((a[j-1] >= a[nach-1]) and (a[j-1] <= a[nach-1] + d)) and ((a[j-1] != a[nach-1]) or (j >= nach)):
                dfs(j,mas,tyt_yge_bili,f,nach)
                f[nomer] = (f[nomer] * (f[j] + 1)) % MOD
                
            
rez = 0
for z in range(1,n+1):
    f = []
    tyt_yge_bili = []
    for _ in range(n+1):
        f.append(0)
        tyt_yge_bili.append(0)
    dfs(z,mas,tyt_yge_bili,f , z)
    rez = (rez + f[z]) % MOD
    

print(rez)





    

