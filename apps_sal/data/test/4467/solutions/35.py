N = int(input())
R = [[0, 0] for _ in range(N)]
B = [[0, 0] for _ in range(N)]
Map = [['.' for __ in range(2*N)] for _ in range(2*N)]
for i in range(N):
  R[i][1], R[i][0] = map(int, input().split())
  Map[R[i][1]][R[i][0]] = 'R'
for i in range(N):
  B[i][0], B[i][1] = map(int, input().split())
  Map[B[i][0]][B[i][1]] = 'B'
R.sort(reverse=True)
B.sort()
RF = [True for _ in range(N)]
BF = [True for _ in range(N)]
cnt = 0
for i in range(N):
  for j in range(N):
    if BF[j] == True:
      if R[i][1] < B[j][0] and R[i][0] < B[j][1]:
        cnt += 1
        RF[i] = False
        BF[j] = False
        break
print(cnt)
