fib = [1, 1, 2, 3, 5, 8, 13, 21]
mod = 1000000007
h, w, k = list(map(int, input().split()))
k -= 1
p = [0] * w
p[0] = 1
for i in range(h):
  q = [0] * w
  for j in range(w):
    if j > 0:
      q[j] += p[j - 1] * fib[j - 1] * fib[w - 1 - j]
    if j < w - 1:
      q[j] += p[j + 1] * fib[j] * fib[w - j - 2]
    if 0 < j < w - 1:
      q[j] += p[j] * fib[j] * fib[w - j - 1]
    elif j > 0:
      q[j] += p[j] * fib[j]
    elif j < w - 1:
      q[j] += p[j] * fib[w - j - 1]
    else:
      q[j] += p[j]
    q[j] %= mod
  p = q
print((p[k]))

