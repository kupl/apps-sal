# -*- coding: UTF-8 -*-
def evaluate(origin_str):
    ans = []
    for i in [1, 2, 3, 4, 6, 12]:
        last_idx = int(12 / i)
        flags = [1 for i in range(0, last_idx)]
        if (i == 1):
            flag = False
            for ch in origin_str:
                if (ch == 'X'):
                    flag = True
            if (flag):
                ans.append([i, last_idx])
        else:
            for j in range(0, last_idx):
                tmp = []
                k = j - last_idx
                for x in range(0, i):
                    k += last_idx
                    tmp.append(k)
                for l in tmp:
                    ch = origin_str[l]
                    if (ch != 'X'):
                        flags[j] = 0
            if (sum(flags) != 0):
                ans.append([i, last_idx])
    s = ""
    for a in ans:
        s += str(a[0]) + "x" + str(a[1]) + " "
    print(str(len(ans)) + " " + s)


def main():
    n = int(input())
    for i in range(0, n):
        evaluate(input())


main()
