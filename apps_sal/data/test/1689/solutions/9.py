n = int(input())
k = []
a = 0
for i in range(n):
    s = input()
    if s[0] == "O" and s[1] == "O" and a == 0:
        a = 1
        k.append("++" + s[2:])
    elif s[3] == "O" and s[4] == "O" and a == 0:
        a = 1
        k.append(s[:-2] + "++")
    else:
        k.append(s)
if a:
    print("YES")
    for i in range(n):
        print(k[i])
else:
    print("NO")
