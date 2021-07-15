H, W = list(map(int, input().split()))
a = []
for i in range(H):
    s = input()
    if "#" in s:
        a.append(s)

d = [i for i in range(W)]

for i in range(W):
    f = 0
    for j in a:
        if j[i] == "#":
            f = 1
            break
    if f == 0:
        d.remove(i)

ans = [""] * H
for i in range(len(a)):
    for j in d:
        ans[i] += a[i][j]
    print((ans[i]))


