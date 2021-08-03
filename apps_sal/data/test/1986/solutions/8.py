n, k = input().split()


f_arr = []
t_arr = []
for a in range(0, int(n)):
    f, t = input().split()
    f_arr.append(int(f))
    t_arr.append(int(t))

# subs_arr=[]
# for l in range (0,int(n)):
# if (t_arr[l]>int(k)):
# subs_arr.append(t_arr[l])
##


# for m in range (0,int(n)):
# if (t_arr[m]<=int(k)):
##        print (max(f_arr))
# if (t_arr[m]>int(k)):
##        print (max(subs_arr))

# for m in range (0,int(n)):
# if (t_arr[m]<=int(k)):
##
##
# if (t_arr[m]>int(k)):
# z2=[]
# z2.append(max(f_arr))
# print (z2[0]) range

joy_arr = []
for l in range(0, int(n)):
    if (t_arr[l] > int(k)):
        joy_arr.append(f_arr[l] - (t_arr[l] - int(k)))
    if (t_arr[l] <= int(k)):
        joy_arr.append(f_arr[l])


print(max(joy_arr))
