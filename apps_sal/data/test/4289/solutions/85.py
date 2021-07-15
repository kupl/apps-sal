n=int(input())
t,a = map(int,input().split())
H = list(map(int,input().split()))
ans = -1
h = 1000
for i in range(n):
  if abs(t-H[i]*0.006-a) < h:
    h = abs(t-H[i]*0.006-a)
    ans = i+1
print(ans)
