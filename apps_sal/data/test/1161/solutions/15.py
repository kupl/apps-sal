from collections import deque
import sys

strv = list(input())

if len(strv) % 2 != 0:
    print("Impossible")
    return

openQ = deque([])

y = 0

for brk in strv:
    if brk in ['[', '{', '(', '<']:
        openQ.append(brk)
    else:
        if len(openQ) >= 1:
            lastIn = openQ.pop()
            if brk == "}":
                if lastIn != "{":
                    y = y + 1
            elif brk == "]":
                if lastIn != "[":
                    y = y + 1
            elif brk == ")":
                if lastIn != "(":
                    y = y + 1
            elif brk == ">":
                if lastIn != "<":
                    y = y + 1
        else:
            y = "Impossible"
            break

if len(openQ) == 0:
    print(y)
else:
    print("Impossible")
