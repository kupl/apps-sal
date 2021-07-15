h, w = map(int, input().split())
src = [input() for i in range(h)]

ans = []
for row in src:
        ans.append(list(row))

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for x in range(h):
        for y in range(w):
                if src[x][y] == ".":
                        continue
                if src[x][y] == "#":
                        flag = 0
                        for dx, dy in dxy:
                                if x + dx < 0 or x + dx > h -1 or y + dy < 0 or y + dy > w - 1:
                                        continue
                                if src[x + dx][y + dy] == "#":
                                        flag = 1
                                        break
                        if flag == 0:
                                print("No")
                                return

print("Yes")
