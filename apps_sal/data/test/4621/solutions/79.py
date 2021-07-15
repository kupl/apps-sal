h, w = list(map(int, input().split()))
c = []
for i in range(h):
    c.append(input())

for i in range(h * 2):
    res = ""
    for j in range(w):
        res += c[i // 2][j]
    print(res)

