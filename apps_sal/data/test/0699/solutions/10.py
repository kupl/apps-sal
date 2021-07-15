
def foo():
   inp = input()
   y, k, n = inp.split()
   y = int(y)
   k = int(k)
   n = int(n)

   count = y // k
   count += 1

   cur = count * k
   if (cur > n):
      print(-1)
   while cur <= n:
      print(cur - y, end = ' ')
      cur += k

foo()
