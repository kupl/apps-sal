s = input()
d = input().split()
p = 0
for i in range(5):
    if d[i][0] == s[0] or d[i][1] == s[1]:
        p += 1
if p:
    print("YES")
else:
    print("NO")

