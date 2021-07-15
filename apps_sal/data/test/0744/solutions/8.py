n = int(input())
s = input()
scount = 0
fcount = 0
for i in range(len(s) - 1):
    if s[i] + s[i + 1] == "SF":
        scount += 1
    elif s[i] + s[i + 1] == "FS":
        fcount += 1
if scount > fcount:
    print("YES")
else:
    print("NO")
