a = input()
t = -1
flag = "False"
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        flag = "True1"
        t = i
        break
    if i != len(a) - 2:
        if a[i] == a[i + 2]:
            flag = "True2"
            t = i
            break
if flag == "False":
    print("{} {}".format(-1, -1))
elif flag == "True1":
    print("{} {}".format(t + 1, t + 2))
else:
    print("{} {}".format(t + 1, t + 3))
