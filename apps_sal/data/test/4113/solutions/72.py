N = int (input ())
x = 'No'
while N >= 0:
  if N%4 == 0:
    x = 'Yes'
    break
  N -= 7
print (x)
