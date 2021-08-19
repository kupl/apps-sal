n = int(input())
a = []
for x in range(n):
    m1 = input()
    m = m1.split(' ')
    b = []
    c = 0
    for y in m:
        if(c != 0):
            b.append(int(y))
        c = c + 1
    a.append(b)
# print(a)
for z in range(n):
    lis1 = a[z]
    #print("list considered is :")
    # print(lis1)
    flag = 3
    count = 0
    for m in a:
        if(z != count):
            if(set(m).issubset(set(lis1))):
                flag = 2
                # break
        count = count + 1
    if(flag == 2):
        print("NO")
    else:
        print("YES")
