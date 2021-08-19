(n, k) = list(map(int, input().split()))
sushi = []
for i in range(n):
    sushi.append(list(map(int, input().split())))
point = 0
sushi_kind = set()
duplication = []
sushi.sort(key=lambda x: x[1], reverse=True)
for i in range(k):
    point += sushi[i][1]
    if sushi[i][0] in sushi_kind:
        duplication.append(sushi[i])
    else:
        sushi_kind.add(sushi[i][0])
ans = point + pow(len(sushi_kind), 2)
dup_index = len(duplication) - 1
for i in range(k, n):
    if sushi[i][0] in sushi_kind:
        continue
    elif dup_index >= 0:
        point -= duplication[dup_index][1]
        dup_index -= 1
        point += sushi[i][1]
        sushi_kind.add(sushi[i][0])
    ans = max(ans, point + pow(len(sushi_kind), 2))
print(ans)
