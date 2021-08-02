w, h, x, y = map(int, input().split(" "))
chu = [w / 2, h / 2]
che = 0
sq = 0
if [x, y] == chu:
    che = 1
sq = h * w / 2
print(sq, che)
