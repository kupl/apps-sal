from sys import stdin as fin

# fin = open("ecr6a.in", "r")

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

sx, sy = abs(x1 - x2), abs(y1 - y2)
print(min(sx, sy) + abs(sx - sy))
