# -*- coding: utf-8 -*-
from collections import deque

s = input()
n = len(s)

ans = eval(s)

for i in range(n):
    if s[i] == '*':
        _s = '(' + s[:i] + ')' + s[i:]
        ans = max(ans, eval(_s))
        _s = s[:i + 1] + '(' + s[i + 1:] + ')'
        ans = max(ans, eval(_s))
        for j in range(i):
            if s[j] == '*':
                _s = s[:j + 1] + '(' + s[j + 1:i] + ')' + s[i:]
                ans = max(ans, eval(_s))

print(ans)
