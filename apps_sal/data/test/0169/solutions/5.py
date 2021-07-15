n = int(input())
a = int(input())
b = int(input())
c = int(input())

cnt1 = n // a
if (n % a >= b):
    cnt1 = cnt1 + 1

cnt2 = 0

k = (n - b) // (b - c)

for mi in range(max(0, k - 10), k + 10, 1):
   if (n - mi * (b - c) >= b):
          cnt2 = mi + 1
          cnt2 = cnt2 + (n - (mi + 1) * (b - c)) // a


print(max(cnt1, cnt2))
