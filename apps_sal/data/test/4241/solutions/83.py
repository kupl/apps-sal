s = input()
t = input()
len_s = len(s)
len_t = len(t)
ini = 0
l_cnt = []
for i in range(len_s - len_t + 1):
    cut = s[i:i + len_t]
    cnt = 0
    for (i, w) in enumerate(t):
        if w != cut[i]:
            cnt += 1
    l_cnt.append(cnt)
print(min(l_cnt))
