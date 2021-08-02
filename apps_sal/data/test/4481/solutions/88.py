n = int(input())

cnt = {}
for i in range(n):
    s = input()
    if s in cnt:
        cnt[s] += 1
    else:
        cnt[s] = 1

res = []

maks = max(list(cnt.items()), key=lambda x: x[1])
for item in list(cnt.items()):
    if item[1] == maks[1]:
        res.append(item[0])

res.sort()
for s in res:
    print(s)
