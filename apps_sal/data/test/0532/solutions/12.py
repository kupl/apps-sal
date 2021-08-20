def count(i, g):
    cost = ord(g) - ord(i)
    if cost < 0:
        cost = 26 + cost
    if cost > 13:
        cost = 26 - cost
    return cost


s = input().strip()
i = 'a'
cnt = 0
for c in s:
    cnt += count(i, c)
    i = c
print(cnt)
