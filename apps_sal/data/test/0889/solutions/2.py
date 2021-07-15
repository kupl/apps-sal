t = [input() for i in range(4)]
ans = 'NO'

for i in range(3):
    for j in range(3):
        s = 0
        for x in range(2):
            for y in range(2):
                s += (t[i + x][j + y] == '.')
        if s != 2:
            ans = 'YES'
            break
print(ans)
