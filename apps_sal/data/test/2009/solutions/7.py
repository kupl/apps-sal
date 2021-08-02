n = int(input())
r1, c1 = list(map(int, input().split()))
r2, c2 = list(map(int, input().split()))
r1 -= 1
r2 -= 1
c1 -= 1
c2 -= 1
maze = []
for i in range(n):
    maze.append(input())
list1 = [(r1, c1)]
list2 = [(r2, c2)]
tovisit = [(r1, c1)]
while len(tovisit) > 0:
    x, y = tovisit.pop()
    for cx, cy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if x + cx >= 0 and y + cy >= 0 and x + cx < n and y + cy < n and (x + cx, y + cy) not in list1 and maze[x + cx][y + cy] == "0":
            list1.append((x + cx, y + cy))
            tovisit.append((x + cx, y + cy))
if (r2, c2) in list1:
    print(0)
    return
tovisit = [(r2, c2)]
while len(tovisit) > 0:
    x, y = tovisit.pop()
    for cx, cy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if x + cx >= 0 and y + cy >= 0 and x + cx < n and y + cy < n and (x + cx, y + cy) not in list2 and maze[x + cx][y + cy] == "0":
            list2.append((x + cx, y + cy))
            tovisit.append((x + cx, y + cy))
mini = 30000000
for i in list1:
    for i2 in list2:
        ans = (i[0] - i2[0])**2 + (i[1] - i2[1])**2
        mini = min(mini, ans)
print(mini)
