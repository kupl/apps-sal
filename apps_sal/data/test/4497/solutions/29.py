n = int(input())
maxCnt = 0
ans = 1

for i in range(1,n+1,1):
    tmpCnt = 0
    j = i
    while j%2 == 0:
        j = j/2
        tmpCnt += 1
    if maxCnt < tmpCnt:
        maxCnt = tmpCnt
        ans = i

print(ans)
