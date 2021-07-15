def func(x):
  if x%2==0:
    return x//2
  else:
    return 3*x + 1
A = [True for i in range(1000001)]
N = int(input())
count = 1
while A[N]:
  A[N] = False
  N = func(N)
  count += 1
print(count)
