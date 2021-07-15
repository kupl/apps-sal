antenna = [input() for _ in range(5)]
k = int(input())

check = True
for i in range(4):
  for j in range(i+1,5):
    if int(antenna[j]) - int(antenna[i]) > k:
      check = False

print("Yay!" if check else ":(")
