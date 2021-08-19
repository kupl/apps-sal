g, d, f = map(int, input().split())

goalkeepers = list(map(int, input().split()))
defenders = list(map(int, input().split()))
forwards = list(map(int, input().split()))


# min goalkeeper
count = 0

for keeper in goalkeepers:
    defend = len(list(filter(lambda x: x > keeper and x <= keeper * 2, defenders)))
    forw = len(list(filter(lambda x: x > keeper and x <= keeper * 2, forwards)))
    count += defend * (defend - 1) * forw * (forw - 1) * (forw - 2) / 12


# min def

for defend in defenders:
    second_defend = len(list(filter(lambda x: x > defend and x <= defend * 2, defenders)))
    forw = len(list(filter(lambda x: x > defend and x <= defend * 2, forwards)))
    goal = len(list(filter(lambda x: x > defend and x <= defend * 2, goalkeepers)))
    count += second_defend * goal * forw * (forw - 1) * (forw - 2) / 6

for defend in forwards:
    second_defend = len(list(filter(lambda x: x > defend and x <= defend * 2, defenders)))
    forw = len(list(filter(lambda x: x > defend and x <= defend * 2, forwards)))
    goal = len(list(filter(lambda x: x > defend and x <= defend * 2, goalkeepers)))
    count += second_defend * (second_defend - 1) * goal * forw * (forw - 1) / 4

print(int(count))
