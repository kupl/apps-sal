(n, s) = input().split()
n = int(n)
ans = 0
for start_ind in range(n):
    a_vs_t = 0
    g_vs_c = 0
    for endInd in range(start_ind, n):
        if s[endInd] == 'A':
            a_vs_t += 1
        elif s[endInd] == 'T':
            a_vs_t -= 1
        elif s[endInd] == 'G':
            g_vs_c += 1
        else:
            g_vs_c -= 1
        if a_vs_t == 0 and g_vs_c == 0:
            ans += 1
print(ans)
