from sys import stdin
n = int(stdin.readline())
a = [int(x) for x in stdin.readline().split()]
visited = [False] * n
visited_count = 0
turns = 0
dir = 1
position = 0
while True:
    if not visited[position] and a[position] <= visited_count:
        visited[position] = True
        visited_count += 1
    if visited_count == n:
        break
    if dir == 1 and position == n - 1 or (dir == -1 and position == 0):
        dir = -dir
        turns += 1
    position += dir
print(turns)
