n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    if i <= 14:
        print("NO")
    else:
        flg = False
        for j in range(1, 7):
            if (i - j) % 14 == 0:
                flg = True
        if flg:
            print("YES")
        else:
            print("NO")
