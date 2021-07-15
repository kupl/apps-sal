tt = int(input())

for loop in range(tt):

    n = int(input())
    a = list(map(int,input().split()))

    cnt = 0
    for i in range(n):

        if a[i] != i+1 and cnt % 2 == 0:
            cnt += 1
        elif a[i] == i+1 and cnt % 2 == 1:
            cnt += 1

    if cnt == 0:
        print(0)
    elif cnt <= 2:
        print(1)
    else:
        print(2)

