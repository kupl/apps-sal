n = int(input())
v =list(map(int, input().split()))
l = [0]*n
s = 0
l = sorted(v)
s = l[0]
for i in range(1,n):
  s = (s+l[i])/2
print(s)
