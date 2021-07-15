N = int(input())
M = [input() for i in range(N)]
 
M_sorted = [''.join(sorted(m)) for m in M]
d = {}
ans = 0
 
for m in M_sorted :
    d.setdefault(m,0)
    ans += d[m]
    d[m] += 1
 
print(ans)
