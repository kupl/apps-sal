n = int(input())
a = []
for _ in range(n):
    a.append(list(input()))

flag = 0
for i in range(n):
    for j in range(1,5):
        if a[i][j]=="O" and a[i][j-1]=="O":
            a[i][j] = "+"
            a[i][j-1] = "+"
            flag =1
            break
    if flag:
        break

if flag:
    print("YES")
    for i in range(n):
        print("".join(str(x) for x in a[i]))
else:
    print("NO")
