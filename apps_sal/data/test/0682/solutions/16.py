
def foo():
   inp = input()
   r1, c1, r2, c2 = map(int, inp.split())
   if (r1 == r2 or c1 == c2):
      print("1", end = " ")
   else:
      print("2", end = " ")

   if ((r1 + c1) % 2) != ((r2 + c2) % 2):
      print("0", end = " ")
   elif (r1 - c1 == r2 - c2 or r1 + c1 == r2 + c2):
      print("1", end = " ")
   else:
      print("2", end = " ")

   print(max(abs(r1 - r2), abs(c1 - c2)))

foo()
