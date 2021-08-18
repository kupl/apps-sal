n = int(input())
num = [int(k) for k in input().split()]
num.sort()
diff = [0] * (n - 1)
for i in range(n - 1):
    diff[i] = num[i + 1] - num[i]

if n == 1:
    print(-1)
else:
    if len(diff) > 1:
        same = True
        for i in range(len(diff) - 1):
            if diff[i] != diff[i + 1]:
                same = False
        if same == True:
            if diff[0] == 0:
                print(1)
                print(num[0])
            else:
                print(2)
                print(num[0] - diff[0], num[n - 1] + diff[0])
        else:
            if diff.count(diff[diff.index(min(diff))]) != len(diff) - 1:
                print(0)
            else:
                if 2 * diff[diff.index(min(diff))] != diff[diff.index(max(diff))]:
                    print(0)
                else:
                    print(1)
                    print(num[diff.index(max(diff))] + diff[diff.index(min(diff))])
    elif len(diff) == 1:
        if diff[0] == 0:
            print(1)
            print(num[0])
        else:
            if (num[0] + num[1]) / 2 % 1 == 0:
                print(3)
                print(num[0] - diff[0], int((num[0] + num[1]) / 2), num[1] + diff[0])
            else:
                print(2)
                print(num[0] - diff[0], num[1] + diff[0])
