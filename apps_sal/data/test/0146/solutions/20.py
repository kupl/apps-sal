n, k = (int(x) for x in input().split())
tabs = [int(x) for x in input().split()]

#print(n, k, tabs)

mods = [sum(tabs[i::k]) for i in range(k)]

# print(mods)

summods = sum(mods)
ans = -1
for i in range(k):
    cand = abs(summods - mods[i])
    if cand > ans:
        ans = cand

print(ans)
