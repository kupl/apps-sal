s = input()
start = 0
goal = 1
while s[start] != "A":
  start += 1
while s[-goal] != "Z":
  goal += 1
print(len(s)-goal-start+1)
