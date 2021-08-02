n = int(input())
wall = list(map(int, input().split()))


# try from left
# try from right
if n == 1:
    print("YES")
else:
    # update all to parity
    in1 = []
    for i in range(n):
        wall[i] = wall[i] % 2
        if(wall[i] == 1):
            in1.append(i)

    if len(in1) == 0 or len(in1) == n:
        print("YES")

    # fix differences in parity
    else:
        if len(in1) == 1:
            if (n - 1) % 2 == 0 and in1[0] % 2 == 0 and (n - in1[0] - 1) % 2 == 0:
                print("YES")
            else:
                print("NO")
        else:
            i = 0
            while(i + 1 < len(in1)):
                if i >= 0 and i + 1 < len(in1) and (in1[i + 1] - in1[i] - 1) % 2 == 0:
                    del in1[i + 1]
                    del in1[i]
                    i -= 1
                else:
                    i += 1
            if len(in1) == 0:
                print("YES")
            elif len(in1) == 1:
                if (n - 1) % 2 == 0 and in1[0] % 2 == 0 and (n - in1[0] - 1) % 2 == 0:
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")
