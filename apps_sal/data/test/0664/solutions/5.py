def s(a, i):
   s = i
   while i+1 < len(a):
      if a[i] <= a[i+1]:
         i += 1
      else:
        return a[s:i+1]
   return a[s:i+1]

n = int(input())
a = list(map(int,input().split()))
b = s(a,0)
c = s(a,len(b))
if len(b) == n:
   print(0)
elif len(b) + len(c) == n and c[len(c)-1] <= b[0]:
    print(len(c))
else:
   print(-1)

