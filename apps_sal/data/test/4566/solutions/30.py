lst1 = input().split()

N = int(lst1[0])
M = int(lst1[1])

lst2 = []

for i in range(M):
   lst2.append(input().split())

lst3 = []
for i in range(N):
   lst3.append(0)

for i in range(M):
   for j in range(2):
      lst3[ int(lst2[i][j]) - 1 ] += 1

for i in range(N):
   print(lst3[i])
