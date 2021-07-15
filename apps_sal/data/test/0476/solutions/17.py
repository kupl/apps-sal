import re
line = input()
match = re.match("([1][4]{0,2})+",line)
if match and match.group(0) == line:
    print("YES")
else:
    print("NO")
