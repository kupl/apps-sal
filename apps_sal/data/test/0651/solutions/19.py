
import itertools


def check(dirs, inst, maze, s):
    posy, posx = s
    rx = len(maze[0])
    ry = len(maze)
    for i in inst:
        if dirs[i] == "N":
            posy -= 1
        elif dirs[i] == "S":
            posy += 1
        elif dirs[i] == "E":
            posx += 1
        elif dirs[i] == "W":
            posx -= 1
        if posx < 0 or posx >= rx or posy < 0 or posy >= ry:
            return False
        if maze[posy][posx] == "
        return False
        if maze[posy][posx] == "E":
            return True
    return False


n, m = list(map(int, input().split()))
maze = []
for i in range(n):
    l = input().strip()
    maze.append(l)
    if "S" in l:
        s = (i, l.index("S"))
inst = list(map(int, input().strip()))
t = 0
for i in itertools.permutations("NWSE"):
    c = check(i, inst, maze, s)
    t += check(i, inst, maze, s)
print(t)
