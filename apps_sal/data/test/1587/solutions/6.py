from collections import Counter


N = int(input())
c = input()
cntr = Counter(c)

ans = 0
for c, r in zip(c, "R" * cntr["R"]):
    if c != r:
        ans += 1
print(ans)
