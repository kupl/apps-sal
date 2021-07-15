n = int(input())
li = list(map(int,input().split()))
li.sort()
cnt = 0
guu = 0
for j in range(100000):
    guu = 0
    for i in range(len(li)):
        if li[i] % 2 == 0:
            guu += 1
    if guu == n:
        for i in range(len(li)):
            li[i] = li[i]//2
        cnt += 1
    else:
        print(cnt)
        return

