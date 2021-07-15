n = int(input())
s = input()

mozi = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for x in s:
  number = mozi.index(x) + n
  if number > 25:
    number = number - 26
  print(mozi[number], end="")
  
