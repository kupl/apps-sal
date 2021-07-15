n = int(input())
a = [int(x) for x in input().split()]
s = 0
s = a[0] * (n - a[0] + 1)
for i in range(len(a)-1):
   if a[i] < a[i+1]:
      s += (a[i+1]-a[i])*(n-a[i+1]+1)
   elif a[i] > a[i+1]:
      s += (a[i]-a[i+1])*a[i+1]
print(s)

