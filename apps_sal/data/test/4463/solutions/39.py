s = input()
t = input()

s_list = list(s)
t_list = list(t)

s_sorted = sorted(s_list)
t_sorted = sorted(t_list, reverse=True)

s_joined = ''.join(s_sorted)
t_joined = ''.join(t_sorted)

if s_joined < t_joined:
    print("Yes")
else:
    print("No")
