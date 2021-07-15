A = [list(map(int, input().split())) for i in range(3)]
N = int(input())
B = [int(input())for i in range(N)]
sheet = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(N):
  for j in range(3):
    for k in range(3):
      if B[i] == A[j][k]:
        sheet[j][k] = 1
if sheet[0][0] == 1 and sheet[0][1] == 1 and sheet[0][2] == 1:
  print('Yes')
elif sheet[1][0] == 1 and sheet[1][1] == 1 and sheet[1][2] == 1:
  print('Yes')
elif sheet[2][0] == 1 and sheet[2][1] == 1 and sheet[2][2] == 1:
  print('Yes')
elif sheet[0][0] == 1 and sheet[1][0] == 1 and sheet[2][0] == 1:
  print('Yes')
elif sheet[0][1] == 1 and sheet[1][1] == 1 and sheet[2][1] == 1:
  print('Yes')
elif sheet[0][2] == 1 and sheet[1][2] == 1 and sheet[2][2] == 1:
  print('Yes')
elif sheet[0][0] == 1 and sheet[1][1] == 1 and sheet[2][2] == 1:
  print('Yes')
elif sheet[2][0] == 1 and sheet[1][1] == 1 and sheet[0][2] == 1:
  print('Yes')
else:
  print('No')
