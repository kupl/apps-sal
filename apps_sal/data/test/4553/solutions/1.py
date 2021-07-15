A, B = map(int, input().split())
S = input()
D = [ str(i) for i in range(10)]
T = S[:A] + S[A+1:]

if S[A] == "-" and all( t in D for t in T):
  print("Yes")
else:
  print("No")
