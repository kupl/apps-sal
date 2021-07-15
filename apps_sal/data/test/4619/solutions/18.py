lst = input().split()

W = int(lst[0])
H = int(lst[1])
N = int(lst[2])

field = [([0] * W)] * H

L = []

for i in range(N):
   L = input().split()
   if L[2] == '1':
      for j in range(H):
         for k in range(int(L[0])):
            field[j][k] = 1
   elif L[2] == '2':
      for j in range(H):
         for k in range(int(L[0]), W):
            field[j][k] = 1
   elif L[2] == '3':
      for j in range(int(L[1])):
         field[j] = [1] * W
   elif L[2] == '4':
      for j in range(int(L[1]), H):
         field[j] = [1] * W

ans = 0

for s in field:
   ans += s.count(0)

print(ans)
