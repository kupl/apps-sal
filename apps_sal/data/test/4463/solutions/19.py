s,t = [input() for i in range(2)]

s_2 = sorted(s)
t_2 = sorted(t,reverse=True)

if s_2 < t_2:
    print("Yes")
else:
    print("No")
