(n, m) = map(int, input().split())
colors = [0] * n


def setColors(a):
    for i in a:
        if colors[i - 1] == 0:
            for c in range(1, 4):
                for j in a:
                    if i != j and c == colors[j - 1]:
                        break
                else:
                    colors[i - 1] = c
                    break


for i in range(m):
    setColors(list(map(int, input().split())))
print(' '.join(map(str, colors)))
