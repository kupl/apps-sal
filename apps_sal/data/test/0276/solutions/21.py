t = int(input())
d = {"red": "Reality", "purple": "Power", "green": "Time", "blue": "Space", "orange": "Soul", "yellow": "Mind"}
l = list(d.values())
for i in range(t):
    r = input()
    l.remove(d[r])
print(len(l))
for y in l:
    print(y)
