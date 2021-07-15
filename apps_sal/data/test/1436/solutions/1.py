n = int(input())
a = [int(i) for i in input().split()]
cnt = 0
cntpols = 0
for i in range(len(a)):
    if a[i] == -1:
        if cntpols == 0:
            cnt += 1
        else:
            cntpols -= 1
    else:
        cntpols += a[i]
print(cnt)
