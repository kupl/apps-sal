n = int(input())
d,x = list(map(int,input().split()))
ans = x
l = []
for i in range(n):
  l.append(int(input()))
for i in l:
  ans += 1 + (d-1)//i
print(ans)
  

