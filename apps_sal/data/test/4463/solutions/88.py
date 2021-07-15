s = input()
t = input()
import sys
if s==t:
    print("No")
    return
ss = sorted(list(s))
tt = sorted(list(t))[::-1]
if sorted([ss,tt])[0] == ss:
    print("Yes")
else:
    print("No")
