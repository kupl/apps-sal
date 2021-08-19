#! /usr/bin/python3


def solve():
    s = input()
    t = input()

    ls = len(s)
    if s[ls - 1] == '\n':
        ls = ls - 1
    lt = len(t)
    if t[lt - 1] == '\n':
        lt = lt - 1

    #print("ls = ",ls," lt = ", lt)
    i = 0
    j = 0
    pos = -1
    while 1:
        if s[i] == t[j]:
            i = i + 1
            j = j + 1
        else:
            j = j + 1

        if i == ls:
            pos = j

        if i == ls or j == lt:
            break

    if pos == -1:
        print(0)
        return
    i = ls - 1
    j = lt - 1
    reverse = -1

    while 1:
        if s[i] == t[j]:
            i = i - 1
            j = j - 1
        else:
            j = j - 1

        if i == -1:
            reverse = j

        if i == -1 or j == -1:
            break
    # print("pos = ",pos,"  reverse = ", reverse)
    reverse = reverse + 1
    pos = pos - 1
    if reverse == -1 or reverse < pos:
        print(0)
    else:
        print(reverse - pos)


solve()
