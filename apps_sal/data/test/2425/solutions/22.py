q = int(input())
for i in range(q):
    a = int(input())
    a_bin = format(a, "b")
    if len(a_bin) == a_bin.count("1"):
        flag = 0
        for j in range(2, int(a**(1/2))+2):
            if a % j == 0:
                print(a//j)
                flag = 1
                break
        if flag == 0:
            print(1)
    else:
        print(2**(len(a_bin))-1)

