n = int(input())
d,x = list(map(int,input().split()))

a = [int(input()) for _ in range(n)]

sum = x

for i in range(n):
  if d%a[i] == 0:
    sum += d//a[i]
  else:
    sum  += d//a[i] +1

print(sum)

