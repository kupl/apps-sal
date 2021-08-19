3
# -*- coding: utf-8 -*-


def check(s):
    if dict_x[s[0]] == 0 and dict_x[s[1]] == 0:
        return "NOT"
    elif dict_x[s[0]] > 0 and dict_x[s[1]] == 0:
        return s[1]
    elif dict_x[s[0]] == 0 and dict_x[s[1]] > 0:
        return s[0]
    elif dict_x[s[0]] == 1 and dict_x[s[1]] == 1:
        return "EVEN"
    else:
        if dict_x[s[0]] > dict_x[s[1]]:
            return s[1]
        else:
            return s[0]


def update(s, mozi):
    if s[1] == mozi:
        dict_x[s[0]] -= 1
        dict_x[s[1]] += 1
    else:
        dict_x[s[0]] += 1
        dict_x[s[1]] -= 1


n, a, b, c = map(int, input().split())
dict_x = {"A": a, "B": b, "C": c}
s_list = []
ans_list = []
flag = 1
for i in range(0, n):
    s = input()
    s_list.append(s)
if a + b + c == 0:
    flag = 0
elif a + b + c == 1:
    for s in s_list:
        x = check(s)
        if x == "NOT":
            flag = 0
            break
        else:
            ans_list.append(x)
            update(s, x)
elif a + b + c == 2:
    i = 0
    for s in s_list:
        x = check(s)
        if x == "NOT":
            flag = 0
            break
        elif x == "EVEN":
            if i == len(s_list) - 1:
                ans_list.append(s[0])
                update(s, x)
            elif s == s_list[i + 1]:
                ans_list.append(s[0])
                update(s, x)
            else:
                if s[0] in s_list[i + 1]:
                    ans_list.append(s[0])
                    update(s, s[0])
                else:
                    ans_list.append(s[1])
                    update(s, s[1])
        else:
            ans_list.append(x)
            update(s, x)
        i += 1
else:
    for s in s_list:
        x = check(s)
        if x == "NOT":
            flag = 0
            break
        elif x == "EVEN":
            ans_list.append(s[0])
            update(s, s[0])
        else:
            ans_list.append(x)
            update(s, x)

if flag == 1:
    print("Yes")
    for ans in ans_list:
        print(ans)
else:
    print("No")
