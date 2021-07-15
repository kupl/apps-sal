n,m = map(int, input().split())
res = [0 for i in range(n)]
P = [0 for i in range(n)]
ans = 0
p = 0
 
for i in range(m) :
    pi, si = input().split()
    pi = int(pi) - 1
    if(res[pi]) :
        continue
    if(si == "AC") :
        res[pi] = 1
        ans += 1
        p += P[pi]
    else :
        P[pi] += 1
print(ans, p)
