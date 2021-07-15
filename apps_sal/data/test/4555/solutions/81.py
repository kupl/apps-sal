a, b, k = map(int, input().split())
n = b - a + 1

if n > k * 2:
  for i in range(k):
    print(a+i)
  for i in range(k):
    print(b-(k-i-1))
else:
  for i in range(a, b+1):
    print(i)
