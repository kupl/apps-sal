n = int(input())
a = [input() for i in range(n)]
ans = False
for i in range(n):
    if ((a[i][0] == "O" and a[i][1] == "O") and not ans):
        a[i] = "++" + a[i][2:]
        ans = True
        continue
    if ((a[i][3] == "O" and a[i][4] == "O") and not ans):
        a[i] = a[i][:3] + "++"
        ans = True
        continue
if (ans):
    print("YES")
    for i in range(n):
        print(a[i])
else:
    print("NO")
