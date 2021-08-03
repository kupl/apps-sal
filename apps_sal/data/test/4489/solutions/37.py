N = int(input())
blue = [input() for _ in range(N)]
M = int(input())
red = [input() for _ in range(M)]

set_blue = set(blue)
scores = []
for s in set_blue:
    score = blue.count(s) - red.count(s)
    scores.append(score)

ms = max(scores)
if ms >= 0:
    print(ms)
else:
    print(0)
