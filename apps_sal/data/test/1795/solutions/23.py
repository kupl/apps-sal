n = int(input())

lst = []
for x in input().split():
    lst.append(int(x) - 1)

flag = False
for x in range(len(lst)):
    if x == lst[lst[lst[x]]]:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")

