from collections import Counter
n = int(input())
a = Counter(list(map(int, input().split())))
cnt = 0
for x, y in a.items():
    if x == y:
        continue
    if x > y:
        cnt += y
    else:
        cnt += y - x
print(cnt)
