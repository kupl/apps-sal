from sys import stdin
n, a, b = [int(x) for x in stdin.readline().rstrip().split()]
sum = 0

for x in range(1,n+1):
   l = x // 10000
   m = (x % 10000) // 1000
   n = (x % 1000) // 100
   o = (x % 100) // 10
   p = x % 10
   if l+m+n+o+p >= a and l+m+n+o+p <= b:
      sum += x

print(sum)
