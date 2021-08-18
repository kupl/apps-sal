from sys import stdin

s = stdin.readline().strip()

s1 = stdin.readline().strip()
a = ["a", "e", "i", "o", "u"]
if len(s) != len(s1):
    print("No")
    return
t = True
for i in range(len(s)):
    if s[i] not in a and s1[i] in a:
        t = False
    if s1[i] not in a and s[i] in a:
        t = False
if t:
    print("Yes")
else:
    print("No")
