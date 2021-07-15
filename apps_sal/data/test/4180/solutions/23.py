N = int(input())
if N % 1000 == 0:
   print("0")
elif N >= 1 and N < 1000:
   print(1000 - (N % 1000))
elif N >= 1000 and N <= 10000:
   print(1000 - (N % 1000))
