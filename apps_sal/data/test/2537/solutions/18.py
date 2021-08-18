import sys
import math

q = int(input())

for x in range(q):
    s = input()
    t = input()
    p = input()

    tc = [0] * 26
    pc = [0] * 26
    for i in range(len(p)):
        pc[ord(p[i]) - 97] += 1

    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1

    if i == len(s):
        for y in range(len(t)):
            tc[ord(t[y]) - 97] += 1
        for y in range(len(s)):
            tc[ord(s[y]) - 97] -= 1

        flag = True
        for y in range(26):
            if pc[y] < tc[y]:
                flag = False
                print("NO")
                break
        if flag:
            print("YES")

    else:
        print("NO")
