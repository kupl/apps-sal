import math
s = input()
s = int(s.replace(" ", ''))
if math.sqrt(s) == int(math.sqrt(s)):
    print("Yes")
else:
    print("No")

