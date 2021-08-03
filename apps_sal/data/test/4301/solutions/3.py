n = int(input())
a_l = [int(input()) for _ in range(n)]

l = []
r = []
l_max = 0
r_max = 0
for i in range(n):
    l_max = max(l_max, a_l[i])
    r_max = max(r_max, a_l[-i - 1])
    l.append(l_max)
    r.append(r_max)
for i in range(n):
    if i == 0:
        t_l = 0
    else:
        t_l = l[i - 1]
    if i == n - 1:
        t_r = 0
    else:
        t_r = r[-i - 2]
    print(max([t_l, t_r]))
