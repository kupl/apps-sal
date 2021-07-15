from collections import Counter

s = Counter(input())
w = Counter("Bulbasaur")

ans = 10 ** 5

for x, y in w.most_common():
    ans = min(ans, s[x] // y)

print(ans)

