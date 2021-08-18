n, k = (int(x) for x in input().split())
tabs = [int(x) for x in input().split()]


mods = [sum(tabs[i::k]) for i in range(k)]


summods = sum(mods)
ans = -1
for i in range(k):
    cand = abs(summods - mods[i])
    if cand > ans:
        ans = cand

print(ans)
