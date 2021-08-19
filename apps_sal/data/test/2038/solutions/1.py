input()
p = [int(x) - 1 for x in input().split()]
pos = [0] * len(p)
for (i, x) in enumerate(p):
    pos[x] = i
ans = []
for (i, x) in enumerate(p):
    if i == x:
        continue
    i_pos = pos[i]
    if 2 * abs(i_pos - i) < len(p):
        if 2 * i_pos >= len(p) and 2 * i >= len(p):
            ans.append((0, i_pos))
            ans.append((0, i))
            ans.append((0, i_pos))
        elif 2 * (len(p) - 1 - i_pos) >= len(p) and 2 * (len(p) - 1 - i) >= len(p):
            ans.append((len(p) - 1, i_pos))
            ans.append((len(p) - 1, i))
            ans.append((len(p) - 1, i_pos))
        else:
            fi = min(i_pos, i)
            la = max(i_pos, i)
            ans.append((fi, len(p) - 1))
            ans.append((0, len(p) - 1))
            ans.append((0, la))
            ans.append((0, len(p) - 1))
            ans.append((fi, len(p) - 1))
    else:
        ans.append((i, i_pos))
    (p[i_pos], p[i]) = (p[i], p[i_pos])
    (pos[p[i_pos]], pos[p[i]]) = (pos[p[i]], pos[p[i_pos]])
print(len(ans))
for (a, b) in ans:
    print(a + 1, b + 1)
assert sorted(p) == p
