s = input()
g_cnt, p_cnt = 0, 0
ans = 0
for c in s:
    if c == 'g':
        if g_cnt > p_cnt:
            ans += 1
            p_cnt += 1
        else:
            g_cnt += 1
    else:
        if g_cnt > p_cnt:
            p_cnt += 1
        else:
            ans -= 1
            g_cnt += 1
print(ans)
