N = int(input())
T, A = map(int, input().split())
for i in range(N-1):
  t, a = map(int, input().split())
  p = (T-1)//t + 1
  q = (A-1)//a + 1
  n = max(p, q)
  T = n*t
  A = n*a
print(T+A)
