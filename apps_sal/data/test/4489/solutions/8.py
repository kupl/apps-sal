n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
ans = 0
l = list(set(s))
for i in range(len(l)):
    ans = max(ans,s.count(l[i])-t.count(l[i]))
print(ans)        
