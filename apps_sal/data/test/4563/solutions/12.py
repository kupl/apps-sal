T = 1
A = 1

for n in range(int(input())):
  t,a = map(int,input().split())
  m = max(-(-T//t),-(-A//a))
  T = m*t
  A = m*a

print(T+A)
