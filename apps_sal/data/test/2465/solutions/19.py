l = []
for i in range(3, 361):
    l.append([])
    x = 180 / i
    for j in range(1, i - 1):
        l[-1].append(x * j)

for _ in range(int(input())):
    x = int(input())
    flag = False
    for i in range(len(l)):
        if x in l[i]:
            print(i + 3)
            flag = True
            break
    if flag == False:
        print(-1)
