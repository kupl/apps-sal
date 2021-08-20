from sys import stdin
tt = int(stdin.readline())
for loop in range(tt):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    z = 0
    o = 0
    ans = []
    for i in a:
        if i == 0:
            z += 1
        else:
            o += 1
        if z == 2:
            z = 0
            o = 0
            ans.append(0)
            ans.append(0)
        elif o == 2:
            z = 0
            o = 0
            ans.append(1)
            ans.append(1)
    if z > 0:
        ans.append(0)
    print(len(ans))
    print(*ans)
