n, k = input().split()


f_arr = []
t_arr = []
for a in range(0, int(n)):
    f, t = input().split()
    f_arr.append(int(f))
    t_arr.append(int(t))


joy_arr = []
for l in range(0, int(n)):
    if (t_arr[l] > int(k)):
        joy_arr.append(f_arr[l] - (t_arr[l] - int(k)))
    if (t_arr[l] <= int(k)):
        joy_arr.append(f_arr[l])


print(max(joy_arr))
