A = [list(map(int,input().split())) for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]
c = [[0]*3 for _ in range(3)]
for x in b:
  for i in range(3):
    for j in range(3):
      if A[i][j] == x:
        c[i][j] = 1

if c[0] == [1,1,1] or c[1] == [1,1,1] or c[2] == [1,1,1]:
  print("Yes")
elif [c[0][0], c[1][0], c[2][0]] == [1,1,1] or [c[0][1], c[1][1], c[2][1]] == [1,1,1] or [c[0][2], c[1][2], c[2][2]] == [1,1,1]:
  print("Yes")
elif [c[0][0], c[1][1], c[2][2]] == [1,1,1] or [c[2][0], c[1][1], c[0][2]] == [1,1,1]:
  print("Yes")
else:
  print("No")
