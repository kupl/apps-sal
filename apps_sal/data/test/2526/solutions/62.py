x,y,a,b,c = map(int, input().split())
l = [list(map(int, input().split())) for i in range(3)]
k = sorted(l[0],reverse=True)[:x]
for i in sorted(l[1],reverse=True)[:y]:
  k.append(i)
for i in l[2]:
  k.append(i)
m = sorted(k,reverse=True)[:x+y]
print(sum(m))
