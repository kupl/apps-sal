A,B,C = map(int,input().split())
K = int(input())

max_num = max(A,B,C)
if A == max_num:
  print(A * (2 ** K) + B + C)
elif B == max_num:
  print(B * (2 ** K) + A + C)
else:
  print(C * (2 ** K) + B + A)
