n, k = list(map(int, input().split()))
s = list(map(int, input().split()))
maxi = 0
pos = n - 1
if n == 1:
    print(s[0])
else:
 if k >= n:
     print(s[-1])
 else:
  while 2 * (k - 1) >= (n - 1):
      maxi = max(maxi, s[pos])
      pos -= 1
      k -= 1
      n -= 1
  posq = 0
  while pos - posq >= 1:
      maxi = max(maxi, s[posq] + s[pos])
      pos -= 1
      posq += 1
  if pos == posq:
      maxi = max(maxi, s[pos])
  print(maxi)

