#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

s = list(str(input()))
t = list(str(input()))

ans = []
for i in range(len(s)-len(t)+1):
    # print(i)
    ans_tmp = ""
    for j in range(len(s)):
        if j >= i and i+len(t) > j:
            if s[j] == "?" or s[j] == t[j-i]:
                ans_tmp += t[j-i]
            else:
                break
        else:
            if s[j] == "?":
                ans_tmp += "a"
            else:
                ans_tmp += s[j]

    if len(ans_tmp) != len(s):
        continue
    else:
        ans.append(ans_tmp)
ans.sort()

if len(ans) == 0:
    print("UNRESTORABLE")
else:
    print((ans[0]))

