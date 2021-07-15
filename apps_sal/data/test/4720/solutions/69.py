N = int(input())
a = 0
for i in range(N):
  line = list(map(int,input().split()))
  a +=(line[-1]-line[0]+1)
print(a)
