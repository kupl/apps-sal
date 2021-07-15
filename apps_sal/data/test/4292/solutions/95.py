n, need = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
ans = 0

for i in range(need):
    ans += li[i]
    
print(ans)
