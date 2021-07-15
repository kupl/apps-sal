N = int(input())
red = [list(map(int, input().split())) for _ in range(N)]
blue = [list(map(int, input().split())) for _ in range(N)]
blue = sorted(blue, key=lambda x: x[0])

used = []
for i in range(N):
    c, d = blue[i]
    m, tmp = -1, -1
    for j in range(N):
        if j in used:
            continue
        a, b = red[j]
        if a < c and b < d:
            if b > m:
                m = b
                tmp = j
    if tmp != -1:
        used.append(tmp)
print(len(used))
