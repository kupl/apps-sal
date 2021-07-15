n,m = map(int, input().split())
step = []

now = 0
for i in range(m):
  next = int(input()) - 1
  step.append(next - now)
  now = next + 2

step.append(n-now)  
step.sort()

def fibo():
  s = []
  a = 1
  b = 1
  s.append(a)
  s.append(b)
  for i in range(n):
    c = a+b
    a = b
    b = c
    s.append(c)
  return s

ans = 1

if step[0] < 0:
  ans = 0

else:
  f = fibo()
  for i in step:
    ans *= f[i]

print(ans % 1000000007)
