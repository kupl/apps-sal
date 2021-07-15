N,M = list(map(int,input().split()))
li = []
for _ in range(M):
  li += input().split()
for i in range(1,N+1):
  print((li.count(str(i))))

