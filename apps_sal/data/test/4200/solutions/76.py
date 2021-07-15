n,m = map(int,input().split())
a = list(map(int,input().split()))

s = sum(a)
a.sort(reverse=True)

for i in range(m):
  if a[i] < s/(4*m):
    print("No")
    return
print("Yes")
