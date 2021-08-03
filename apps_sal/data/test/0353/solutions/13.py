n = int(input())
d = input().split()
d = [int(x) for x in d]
if n == 1 and int(d[0]) != 15 and int(d[0]) != 0:
    print(-1)
elif n == 1 and int(d[0]) == 0:
    print("UP")
elif n == 1 and int(d[0]) == 15:
    print("DOWN")
else:
    if (d[-1] > d[-2] and d[-1] != 15) or d[-1] == 0:
        print("UP")
    elif (d[-1] < d[-2] and d[-1] != 0) or d[-1] == 15:
        print("DOWN")
