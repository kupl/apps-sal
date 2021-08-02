a, b, c = map(int, input().split())

ganma = a % b
if ganma == 0:
    if ganma == c:
        print("YES")
    else:
        print("NO")

else:
    mod_list = []
    for i in range(b):
        mod = (i * ganma) % b
        mod_list.append(mod)

    zero_one_list = []
    for i in range(b):
        if mod_list[i] == c:
            zero_one_list.append(1)
        else:
            zero_one_list.append(0)

    sum_list = sum(zero_one_list)

    if sum_list >= 1:
        print("YES")
    else:
        print("NO")
