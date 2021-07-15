n = int(input())
a = [int(x) for x in input().split()]

def check(p):
  c = 0
  while p % 2 == 0:
    c += 1
    p //= 2
  return c

res = 0
for i in range(n):
  res += check(a[i])
print(res)
