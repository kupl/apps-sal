t = int(input())
list1 = []
arr = list(map(int, input().split()))
for i in range(t):
    for j in range(4):
        if j == 0:
            list1.append(1)
            print(list1[-1], end=" ")
            for x in range(1, arr[i]):
                list1.append((list1[-1] * 2) + 2)
                print(list1[-1], end=" ")
            print()
        elif j == 1:
            list1.append(2)
            print(list1[-1], end=" ")
            for x in range(1, arr[i]):
                list1.append((list1[-1] * 2) + 1)
                print(list1[-1], end=" ")
            print()
        elif j == 2:
            list1.append(4)
            print(list1[-1], end=" ")
            for x in range(1, arr[i]):
                list1.append((list1[-1] * 2) + 2)
                print(list1[-1], end=" ")
            print()
        elif j == 3:
            list1.append(3)
            print(list1[-1], end=" ")
            for x in range(1, arr[i]):
                list1.append(list1[-1] * 2)
                print(list1[-1], end=" ")
            print()
