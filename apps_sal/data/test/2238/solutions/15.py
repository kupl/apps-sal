n = int(input())
k = 1
m = 1
for i in range(n//2 + 1):
   s = ''
   for j in range((n-k)//2):
      s += '*'
   for j in range(k):
      s += 'D'
   for j in range((n-k)//2):
      s += '*'
   k += 2
   print(s)

k -= 4
for i in range(n//2):
   s = ''
   for j in range((n-k)//2):
      s += '*'
   for j in range(k):
      s += 'D'
   for j in range((n-k)//2):
      s += '*'
   k -= 2
   print(s)
