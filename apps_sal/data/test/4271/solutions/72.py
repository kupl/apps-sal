n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
ans = sum(b)
for i in range(1,n):
  if a[i-1]+1 == a[i]:
    ans += c[a[i-1]-1]
print(ans)
