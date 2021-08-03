H, W = map(int, input().split())

h_set = set()
w_set = set()
B = [input() for i in range(H)]
for i in range(H):
    for j in range(W):
        if B[i][j] == '#':
            w_set.add(j)
            h_set.add(i)

for i in range(H):
    if i in h_set:
        t = ""
        for j in range(W):
            if j in w_set:
                t += B[i][j]
        print(t)
