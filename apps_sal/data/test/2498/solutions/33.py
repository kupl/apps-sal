from fractions import gcd
N, M = list(map(int, input().split()))
A = list(map(lambda x: int(x),input().split()))

cnt = [0 for _ in range(N)]
for i in range(N):
  a = A[i]
  while a%2 == 0:
    a = a // 2
    cnt[i] += 1

if max(cnt) > min(cnt):
  print(0)
  return
C = max(cnt)

A = list(map(lambda x: x // pow(2,C), A))
def gcd(a,b):
  if a<b:
    a,b = b,a
  while a%b > 0:
    a,b = b,a%b
  return b

def lcm(a,b):
  return a*b//gcd(a,b)

x = A[0]
for a in A[1:]:
  x = lcm(x,a)
x = x * pow(2,C-1)

print((M // x + 1) // 2)
