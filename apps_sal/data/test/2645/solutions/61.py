s = str(input())
n = len(s)
g_num = 0
p_num = 0
win = 0
lose = 0
for i in range(n):
    if s[i] == 'g' and g_num >= p_num + 1:
        p_num += 1
        win += 1
    elif s[i] == 'g':
        g_num += 1
    elif s[i] == 'p' and g_num >= p_num + 1:
        p_num += 1
    else:
        g_num += 1
        lose += 1
print(win - lose)
