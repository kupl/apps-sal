a, b = list(map(int, input().split(' ')))
string = input()
chars = [x for x in string]
chars2 = set(chars)
chars2 = sorted(chars2, key=lambda x: chars.count(x))
chars2.reverse()

count = [chars.count(x) for x in chars2]
points = 0
cards = 0
for i in range(len(count)):
    if cards + count[i] >= b:
        break
    else:
        cards += count[i]
        points += count[i]**2
points += (b - cards)**2
print(points)
