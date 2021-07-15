h, w = map(int, input().split())
s = [input() for  i in range(h)]

ans  =[]
for row in s:
        ans.append(list(row))
        
dxy = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
for x in range(h):
        for y in range(w):
                if s[x][y] == "#":
                        continue
                c = 0
                for dx, dy in dxy:
                        if x +dx < 0 or x +dx > h-1 or y + dy < 0 or y + dy > w-1:
                                continue
                        else:
                                if s[x + dx][y + dy] == "#":
                                        c += 1
                ans[x][y] = c
for row in ans:
        print("".join(list(map(str, row))))
