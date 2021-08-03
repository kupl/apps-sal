n = int(input())

names = dict()

for _ in range(n):
    name = input().strip()
    if name[0] not in names:
        names[name[0]] = 0
    names[name[0]] += 1

cnt = 0
for k, v in names.items():
    prvi = v // 2
    drugi = v - prvi
    cnt += (prvi * (prvi - 1)) // 2
    cnt += (drugi * (drugi - 1)) // 2
print(cnt)
