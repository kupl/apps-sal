def seg_n(n):
   n = int(n)
   if n == 9:
      return 2
   elif n== 8:
      return 1
   elif n== 7:
      return 5
   elif n== 6:
      return 2
   elif n== 5:
      return 4
   elif n== 4:
      return 3
   elif n== 3:
      return 3
   elif n== 2:
      return 2
   elif n== 1:
      return 7
   else:
      return 2
n = input()
summ = 1
f = seg_n(n[0])
z = seg_n(n[1])
print(f*z)

