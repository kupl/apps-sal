from collections import Counter
N,K,L=map(int,input().split())
drive = [-1] * N;train = [-1] * N
def find(List,x):
  if List[x] < 0:
    return x
  List[x] = find(List,List[x])
  return List[x]
def unite(List,x,y):
  if find(List,x) != find(List,y):
    List[find(List,y)] = find(List,x)
for i in range(K+L):
  a, b = map(int,input().split())
  unite(drive if i < K else train,a-1, b-1)
pair = [(find(drive,i), find(train,i)) for i in range(N)]
c =Counter(pair)
print(*[c[pair[i]] for i in range(N)])
