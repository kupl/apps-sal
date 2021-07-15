from sys import stdin, stdout


p, x, y = list(map(int, stdin.readline().strip().split()))

def getScores(s):
    scores = []
    i = (s // 50) % 475

    for g in range(25):
        i = (i * 96 + 42) % 475
        scores.append(26 + i)

    return scores

z = x
count = 0

while True:
    if x > y:
        if p in getScores(x):
            break
        else:
            x += 50
            count += 1
    else:
        x += 50
        count += 1

dcount = 0
dF = False
x = z
while x >= y:
    if p in getScores(x):
        dF = True
        break
    else:
        x -= 50
        dcount += 1

if dF == True or count == 0:
    print(0)
else:
    print(count // 2 + count % 2)


