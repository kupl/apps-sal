h,w,a,b = map(int, input().split())
import math
ans = 0
mod = 10**9+7
l =[i for i in range(1,h+w+2)]
for i in range(1,len(l)-1):
    l[i+1] = l[i+1]*l[i]%mod
l = [1]+ l
gyakugen = [pow(l[i], mod-2, mod) for i in range(1, len(l))]
gyakugen = [1] + gyakugen
for p in range(1, w-b+1):
    ans += l[(h-a-1+b+p-1)]*l[w-(b+p)+a-1]*\
    gyakugen[h-a-1]*gyakugen[b+p-1] * gyakugen[a-1]*gyakugen[w-(b+p)]
print(int(ans)%mod)
