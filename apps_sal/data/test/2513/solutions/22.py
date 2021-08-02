import copy

n = int(input())
s = input()

flag = False
begin_list = [["S", "S"], ["W", "S"], ["S", "W"], ["W", "W"]]

for i in range(4):
    sub = copy.deepcopy(begin_list[i])
    judge = True
    for j in range(2, n):
        if s[j - 1] == "o":
            if sub[j - 1] == "S":
                if sub[j - 2] == "S":
                    sub.append("S")
                else:
                    sub.append("W")
            else:
                if sub[j - 2] == "S":
                    sub.append("W")
                else:
                    sub.append("S")
        else:
            if sub[j - 1] == "S":
                if sub[j - 2] == "S":
                    sub.append("W")
                else:
                    sub.append("S")
            else:
                if sub[j - 2] == "S":
                    sub.append("S")
                else:
                    sub.append("W")
    if s[-1] == "o":
        if (sub[-1] == "S" and sub[-2] != sub[0]) or (sub[-1] == "W" and sub[-2] == sub[0]):
            continue
    else:
        if (sub[-1] == "S" and sub[-2] == sub[0]) or (sub[-1] == "W" and sub[-2] != sub[0]):
            continue
    if s[0] == "o":
        if (sub[0] == "S" and sub[-1] != sub[1]) or (sub[0] == "W" and sub[-1] == sub[1]):
            continue
    else:
        if (sub[0] == "S" and sub[-1] == sub[1]) or (sub[0] == "W" and sub[-1] != sub[1]):
            continue
    flag = True
    break

if flag:
    print("".join(sub))
else:
    print(-1)
