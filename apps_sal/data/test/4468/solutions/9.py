N, T = [int(x) for x in input().split()]
t_list = [int(x) for x in input().split()]
t_s = t_e = ans = 0
for t in t_list:
    if t > t_e:
        ans += t_e - t_s
        t_s = t
    t_e = t + T
ans += t_e - t_s
print(ans)
