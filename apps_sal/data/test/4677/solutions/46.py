# -*- coding: utf-8 -*-

S = list(input())
ans = []

for i in range(len(S)):
    if S[i] == 'B':
        if len(ans) == 0:
            continue
        else:
            ans.pop()
    else:
        ans.append(S[i])

for i in range(len(ans)):
    print(ans[i], end="")

print()
