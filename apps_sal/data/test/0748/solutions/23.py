n = input()
a = [int(i) for i in input().split()]
g = 0
k = [0] * 7
flag = False
k[0] = a.count(1)
k[1] = a.count(2)
k[2] = a.count(3)
k[3] = a.count(4)
k[4] = a.count(5)
k[5] = a.count(6)
k[6] = a.count(7)
if k[0] == k[1] + k[2] == k[3] + k[5] and k[4] + k[6] == 0 and (k[2] <= k[5]) and (k[3] <= k[1]):
    flag = True
else:
    print(-1)
if flag:
    for i in range(k[0]):
        print(1, end=' ')
        if k[2] > 0:
            print(3, end=' ')
            print(6)
            k[5] -= 1
            k[2] -= 1
        else:
            print(2, end=' ')
            if k[5] > 0:
                print(6)
                k[5] -= 1
            else:
                print(4)
