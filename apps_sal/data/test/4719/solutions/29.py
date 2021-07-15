from collections import defaultdict
n = int(input())
new_d = {}
for i in range(ord("a"), ord("z") + 1):
    new_d[chr(i)] = 50
for _ in range(n):
    old_d = new_d
    s = input()
    d = defaultdict(int)
    for c in s:
        if c not in old_d:
            continue
        d[c] += 1
    new_d = {}
    for c in d.keys():
        new_d[c] = min(old_d[c], d[c])
ans = ""
for c, v in sorted(new_d.items()):
    ans += c * v
print(ans)
