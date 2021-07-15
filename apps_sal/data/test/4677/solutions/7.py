x=input()
z=''

for i in x:
  if i == '0':
    z= z+i
  elif i == '1':
    z= z+i
  elif i == 'B':
    z= z[:-1]

print(z)  
