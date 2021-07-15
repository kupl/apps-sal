field=[]
result="Yes"
for i in range(3):
  field.append(list(map(int,input().split())))
for i in range(3):
  for j in range(3):
    if not (field[i][j]>=0 and field[i][j]<=100*2):
      result="No"
    if j ==0:
      pos_i0=field[i][j]
    field[i][j]-=pos_i0
for j in range(3):
  if not (field[0][j]==field[1][j] and field[0][j]==field[2][j]):
    result="No"
print(result)
