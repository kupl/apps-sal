n = int(input())

a = [tuple(map(int, input().split())) for _ in range(n)]
#print(a)
a.sort(key = lambda x : x[1])
max_r = -10**10
ans = 0
for l, r in a:
     if l > max_r:
         ans += 1
         max_r = r
print(ans)
    

