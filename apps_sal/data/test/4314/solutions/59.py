h, w = list(map(int, input().split()))
fields = [list(input()) for _ in range(h)]
ans = [[0] * w] * h
for i in range(h):
    if "#" not in fields[i]:
        ans[i] = [1] * w
for i in range(w):
    count = 0
    for j in range(h):
        if fields[j][i] == ".":
            count += 1
    if count == h:
        for j in range(h):
            ans[j][i] = 1
tmp = []
for out, flag in zip(fields, ans):
    content = []
    for i in range(w):
        if flag[i] == 0:
            content.append(out[i])
    tmp.append(content)
for content in tmp:
    if content != []:
        print(("".join(content)))
