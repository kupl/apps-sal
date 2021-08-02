s = input()

p = "heidi"

idx = 0
for c in s:
    if c == p[idx]:
        idx += 1
        if idx >= len(p): break

ans = ["NO", "YES"][idx == len(p)]
print(ans)
