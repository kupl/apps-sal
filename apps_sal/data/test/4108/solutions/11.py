s = list(input())
t = list(input())
n = len(s)
s_par = [i for i in range(n + 1)]
t_par = [i for i in range(n + 1)]
for i in range(n):
    for j in range(i):
        if s[i] == s[j]:
            s_par[i] = s_par[j]
            break
for i in range(n):
    for j in range(i):
        if t[i] == t[j]:
            t_par[i] = t_par[j]
            break
if s_par == t_par:
    print('Yes')
else:
    print('No')
