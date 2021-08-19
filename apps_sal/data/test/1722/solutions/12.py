from collections import defaultdict


def pairs(n):
    return n * (n - 1) // 2


n = int(input())
names = [input() for _ in range(n)]
letters = defaultdict(int)
for name in names:
    letters[name[0]] += 1
ans = 0
for val in letters.values():
    ans += pairs(val // 2) + pairs(val - val // 2)
print(ans)
