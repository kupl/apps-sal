n = int(input())

aa = []
for i in range(n):
    aa.append(int(input()))
for a in aa:

    flag = True
    for t in range(35):
        if (a - (t*3)) % 7 == 0 and  a - (t*3) >= 0:
            print("YES")
            flag = False
            break
    if flag:
        print("NO")
