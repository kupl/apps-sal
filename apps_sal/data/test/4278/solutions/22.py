from collections import defaultdict as dd

n=int(input())
dic=dd(int)
for i in range(n):
  s=sorted(input())
  dic[''.join(s)]+=1

ans=0  
for v in dic.values():
  ans+=(v)*(v-1)//2
print(ans)
