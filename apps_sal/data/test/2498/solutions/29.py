N, M = list(map(int, input().split()))
a = list(map(int, input().split()))
for k in range(N):
  a[k] //= 2

foo = 1
while a[0]%2 == 0:
  foo *= 2
  a[0] //= 2
for k in range(1, N):
  if a[k] % foo == 0 and a[k]%(2*foo) !=0:
    a[k] //= foo
    continue
  else:
    print((0))
    return
ans = 0

for odd in [3, 5, 7, 11]:
  flag = False
  for k in range(N):
    if a[k]%odd == 0:
      a[k] //= odd
      flag = True
  if flag:
    foo *= odd
 
 
def euclid(a, b):
  while b:
    a, b = b, a%b
  return a

lcm = a.pop()
for k in range(1, N):
  b = a.pop()
  lcm = lcm * b // euclid(lcm, b)
  if lcm* foo > M:
    print((0))
    return
lcm *= foo
ans = int((M / lcm -1)//2 + 1)
print(ans)


