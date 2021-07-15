n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = sum(a)
for i in range(n-1,-1,-1):
  if a[i+1] < b[i]:  
    a[i] = max(0, a[i]-b[i]+a[i+1])
    a[i+1] = 0
  else:
    a[i+1] -= b[i]
print(s-sum(a))
