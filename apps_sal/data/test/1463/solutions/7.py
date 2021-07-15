n = int(input())
data = []
for i in range(n):
    data += [list(map(int, input().split()))]

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            t = True
            continue
        t = False
        for k in range(n):
            for m in range(n):
                if data[i][k] + data[m][j] == data[i][j]:
                    t = True
                    break
        if not t:
            print("No")
            break
    if not t:
        break
if t:
    print("Yes")

