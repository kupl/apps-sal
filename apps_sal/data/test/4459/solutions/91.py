from collections import Counter
n = int(input())
a = Counter(list(map(int, input().split())))
ans = 0
for (x, y) in a.items():
    if x < y:
        ans += y - x
    elif y < x:
        ans += y
print(ans)
