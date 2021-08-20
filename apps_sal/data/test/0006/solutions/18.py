import math
t = int(input())
for _ in range(t):
    (n, inithead) = list(map(int, input().split()))
    dif = []
    desl = []
    for i in range(n):
        (des, hinc) = list(map(int, input().split()))
        dif += [des - hinc]
        desl += [des]
    maxdes = max(desl)
    maxdif = max(dif)
    if maxdes < inithead and maxdif <= 0:
        print(-1)
    else:
        count = 1
        head = inithead - maxdes
        if head > 0:
            count += math.ceil(head / maxdif)
        print(count)
