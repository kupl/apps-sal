h, w, k = map(int, input().split())
maze = []
for i in range(h):
    s = input()
    maze.append([c for c in s])
ans = 0
for i in range(2**(h)):
    for j in range(2**(w)):
        bla = 0
        for column in range(h):
            for line in range(w):
                if (i >> (column) & 1) and (j >> (line) & 1) and maze[column][line] == '
                bla += 1
        if bla == k:
            ans += 1
print(ans)
