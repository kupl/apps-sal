import re

a, b = map(int, input().split())
s = input()
s = re.sub(r"[0-9]", "+", s)
if s[0:a].count("+") == a and s[a] == "-" and s[a + 1:a + b + 1].count("+") == b:
    print("Yes")
else:
    print("No")
