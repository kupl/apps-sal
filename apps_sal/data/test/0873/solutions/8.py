n = int(input())
start = input()
goal = input()
count = 0
for (s, g) in zip(start, goal):
    s = int(s)
    g = int(g)
    count += min(abs(s - g), abs(10 + s - g), abs(10 + g - s))
print(count)
