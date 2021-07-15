N, M = list(map(int, input().split()))
l =set([i for i in range(1, M+1)])
for _ in range(N):
  k, *lst = list(map(int, input().split()))
  l = l & set(lst)
  
print((len(l)))

