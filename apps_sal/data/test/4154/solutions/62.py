N,M = map(int,input().split())
a = list()
b = list()
for i in range(M):
  tmp_a,tmp_b =  map(int, input().split())
  a.append(tmp_a)
  b.append(tmp_b)
print(min(b)-max(a)+1 if min(b)-max(a) >= 0 else 0)
