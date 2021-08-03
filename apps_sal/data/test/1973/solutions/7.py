n = int(input())
arr = list(map(int, input().split()))
d = [0] * 10
max_ = 1
for i in range(n):
    d[arr[i] - 1] += 1
    lol = sorted([x for x in d if x > 0])
    kek = True
    for j in range(len(lol) - 2):
        if lol[j] != lol[j + 1]:
            kek = False
            break
    if kek and len(lol) == 1:
        max_ = max(max_, i + 1)
        continue
    elif kek and lol[-1] - 1 == lol[-2]:
        max_ = max(max_, i + 1)
        continue

    kek = True
    for j in range(1, len(lol) - 1):
        if lol[j] != lol[j + 1]:
            kek = False
            break
    if kek and lol[0] - 1 == 0:
        max_ = max(max_, i + 1)
print(max_)
