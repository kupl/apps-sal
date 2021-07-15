l = sorted(list(map(int, input().split())))
if (l[2] - l[1])%2 == 0 and (l[2] - l[0])%2 == 0:
    print((l[2] - l[1])//2 + (l[2] - l[0])//2)
elif (l[2] - l[1])%2 == 0 and (l[2] - l[0])%2 != 0:
    print((l[2] - l[1])//2 + (l[2] - l[0])//2 + 2)
elif (l[2] - l[1])%2 != 0 and (l[2] - l[0])%2 == 0:
    print((l[2] - l[1])//2 + (l[2] - l[0])//2 + 2)
else:
    print((l[2] - l[1])//2 + (l[2] - l[0])//2 + 1)
