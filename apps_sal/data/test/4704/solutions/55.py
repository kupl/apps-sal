n = int(input())
a = [int(x) for x in input().split()]
s = [0] * (n+2)
for i in range(n):
  s[i+1] = s[i] + a[i]

res = 10 ** 10

for i in range(1,n):
  res = min(res,abs(s[i] - (s[n] - s[i])))

print(res)
