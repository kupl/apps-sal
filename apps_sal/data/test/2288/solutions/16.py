
t = int(input())

for T in range(t):
    n = int(input())

    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    if 0 in b and 1 in b:
        print("Yes")
    else:
        Yes = True
        for i in range(1,n):
            if a[i] < a[i - 1]:
                Yes = False
                break
        if Yes:
            print("Yes")
        else:
            print("No")

