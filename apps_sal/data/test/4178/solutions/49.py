n = int(input())
H = list(map(int, input().split()))
pre = H[-1]
flag = False
if n == 1:
    print("Yes")
else:
    for h in H[-2::-1]:
        if h > pre:
            if h - pre != 1:
                print("No")
                break
            h -= 1
        pre = h
    else:
        print("Yes")
