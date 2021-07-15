x = input().split() # ['0', '2', '3', '4', '5']
x = [ int(i) for i in x ]

for i in range(len(x)):
  if x[i] == 0:
    print(i+1)
