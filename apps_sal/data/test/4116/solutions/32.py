N = int(input())
if(N > 81):
  print("No")
else:
  state='No'
  for i in range(1,10):
    for j in range(1,10):
      if(i*j == N):
        state='Yes'
        break
      if(i*j > N):
        break
  print(state)
