s = input()
flag = 0
ans = 1
aa = s.count("a")
bb = s.count("b")
cc = s.count("c")
if min(aa, bb) == 0 or (bb != cc and aa != cc):
    print("NO")
else:
    for i in s:
        if flag == 0:
            if i == "b":
                flag = 1
                continue
            if i != "a":
                ans = 0
                break
        elif flag == 1:
            if i == "c":
                flag = 2
                continue
            if i != "b":
                ans = 0
                break
        else:
            if i != "c":
                ans = 0
                break
    if ans == 1:
        print("YES")
    else:
        print("NO")
