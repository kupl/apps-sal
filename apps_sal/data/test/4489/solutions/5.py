n = int(input())
blue = []
for i in range(n):
    blue.append(input())
m = int(input())
red = []
for i in range(m):
    red.append(input())
scores = []
for i in range(len(blue)):
    score = blue.count(blue[i]) - red.count(blue[i])
    scores.append(score)

if max(scores) < 0:
    print(0)
else:
    print(max(scores))
