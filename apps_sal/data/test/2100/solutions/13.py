
def foo():
   n = int(input())
   a, b = [], []
   for i in range(n):
      inp = input()
      a1, b1 = inp.split()
      a.append(int(a1))
      b.append(int(b1))

   num1 = sum(a)
   num2 = sum(b)
   num1 = min(num1, n - num1)
   num2 = min(num2, n - num2)

   print(num1 + num2)

foo()
