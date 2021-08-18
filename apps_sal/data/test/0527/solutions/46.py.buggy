s = input()
t = input()
l_s = len(s)
l_t = len(t)

s2 = s + s
l_s2 = len(s2)

next_idx = [[l_s2] * 26 for i in range(l_s2)]

for i in reversed(range(1, l_s2)):
    for j in range(26):
        next_idx[i - 1][j] = next_idx[i][j]
    next_idx[i - 1][ord(s2[i]) - ord("a")] = i

cur_idx = 0
for i in range(l_t):
    if i == 0:
        flg = False
        for j in range(l_s):
            if t[i] == s[j]:
                cur_idx += j
                flg = True
                break
        if flg:
            continue
        else:
            print("-1")
            return

    else:
        idx = next_idx[cur_idx % l_s][ord(t[i]) - ord("a")]

    if idx == l_s2:
        print("-1")
        return

    cur_idx += idx - (cur_idx % l_s)

print(cur_idx + 1)
