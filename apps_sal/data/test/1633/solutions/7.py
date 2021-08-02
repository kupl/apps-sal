bad = []
x = 0
y = 0
asdf = [[False] * 1005 for _ in range(1005)]
a, b, c = map(int, input().split(' '))
for i in range(c):
    x, y = map(int, input().split(' '))
    asdf[x][y] = True

    if asdf[x - 1][y - 1] and asdf[x][y - 1] and asdf[x - 1][y]:
        print(i + 1)
        quit()
    elif asdf[x - 1][y] and asdf[x][y + 1] and asdf[x - 1][y + 1]:
        print(i + 1)
        quit()
    elif asdf[x][y - 1] and asdf[x + 1][y - 1] and asdf[x + 1][y]:
        print(i + 1)
        quit()
    elif asdf[x][y + 1] and asdf[x + 1][y + 1] and asdf[x + 1][y]:
        print(i + 1)
        quit()


print(0)
