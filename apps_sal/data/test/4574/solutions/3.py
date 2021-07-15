from collections import Counter

n = int(input())
a = Counter(map(int, input().split()))
xy = []
a = sorted(a.items(), key=lambda x: x[0], reverse=True)
for i in a:
    if len(xy) == 2:
        break
    if i[1] >= 4:
        xy.append(i[0])
        xy.append(i[0])
        break
    if i[1] >= 2:
        xy.append(i[0])

    else:
        pass
print(xy[0] * xy[1]) if len(xy) >= 2 else print(0)
