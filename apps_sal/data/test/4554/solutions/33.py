W, A, B = [int(i) for i in input().split()]

if B <= A <= B+W or B <= A+W <= B+W or A <= B <= A+W or A <= B+W <= A+W:
  print((0))
elif W + A <= B:
  print((B - (W + A)))
else:
  print((A - (B + W)))

