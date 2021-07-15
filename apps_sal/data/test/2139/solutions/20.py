word = input()
points = 0
y=0
for i in range(len(word)):
    part = word[i:]
    if "bear" in part :
        points += len(part)-(part.index("bear")+3)

print(points)
