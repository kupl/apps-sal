T = int(input().strip())
for t in range(T):
    a, b,c,d  = list(map(int, input().split()))
    if b>=a:
        print(b)
        continue
    if c>d:
        sleeptime = c-d
        remtime = a-b
        stimes = remtime//sleeptime
        if remtime % sleeptime >0:
            stimes += 1
        print(b + c * stimes)
        continue
    else:
        print(-1)
        continue

