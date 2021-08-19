num = int(input())
txt = input()
points = txt.split(' ')
score = [0, 0]
turn = 0
while len(points) > 0:
    maxp = max(int(points[0]), int(points[-1]))
    score[turn] += maxp
    points.remove(str(maxp))
    turn = (turn + 1) % 2
print(score[0], score[1])
