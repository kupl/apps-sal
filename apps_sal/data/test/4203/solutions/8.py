import re
s = input()
if s[0] == "A" and "C" in s[2:-1] and len(re.findall('[A-Z]', s)) == 2:
    print("AC")
else:
    print("WA")
