S = input()
A,B,C,D = int(S[0]),int(S[1]),int(S[2]),int(S[3])

if A+B+C+D == 7:
  print(str(A) + "+" + str(B) + "+" + str(C) + "+" + str(D) + "=7")
  
elif A+B+C-D == 7:
  print(str(A) + "+" + str(B) + "+" + str(C) + "-" + str(D) + "=7")
  
elif A+B-C+D == 7:
  print(str(A) + "+" + str(B) + "-" + str(C) + "+" + str(D) + "=7")
  
elif A+B-C-D == 7:
  print(str(A) + "+" + str(B) + "-" + str(C) + "-" + str(D) + "=7")
  
elif A-B+C+D == 7:
  print(str(A) + "-" + str(B) + "+" + str(C) + "+" + str(D) + "=7")
  
elif A-B+C-D == 7:
  print(str(A) + "-" + str(B) + "+" + str(C) + "-" + str(D) + "=7")
  
elif A-B-C+D == 7:
  print(str(A) + "-" + str(B) + "-" + str(C) + "+" + str(D) + "=7")
  
else:
  print(str(A) + "-" + str(B) + "-" + str(C) + "-" + str(D) + "=7")
