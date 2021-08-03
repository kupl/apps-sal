import sys

n = int(sys.stdin.readline().strip())
m = n // 2
s = sys.stdin.readline().strip()
s1 = 0
s2 = 0
x1 = 0
x2 = 0
for i in range(0, m):
    if s[i] == "?":
        x1 = x1 + 1
    else:
        s1 = s1 + int(str(s[i]))
    if s[m + i] == "?":
        x2 = x2 + 1
    else:
        s2 = s2 + int(str(s[m + i]))
if s1 + (x1 // 2) * 9 == s2 + (x2 // 2) * 9:
    print("Bicarp")
else:
    print("Monocarp")
