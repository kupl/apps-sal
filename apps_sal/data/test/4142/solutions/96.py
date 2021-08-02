s = str(input())
d = True

for i in range(len(s)):
    if i % 2 == 0:
        if s[i] != "R" and s[i] != "U" and s[i] != "D":
            d = False
    else:
        if s[i] != "L" and s[i] != "U" and s[i] != "D":
            d = False
if d:
    print("Yes")
else:
    print("No")
