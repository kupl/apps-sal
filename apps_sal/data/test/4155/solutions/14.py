n = int(input())
h = list(map(int, input().split())) 

ans = 0

for i in range(max(h)):
    if h[0] == 0:
        zeroFlag = True
        for j in range(0, n):
            if h[j] == 0:
                zeroFlag = True
            if h[j] != 0 and zeroFlag == True:
                ans += 1
                zeroFlag = False
            if h[j] > 0:
                h[j] -= 1
    else:
        numFlag = True
        for j in range(0, n):
            if h[j] == 0:
                numFlag = True
            if h[j] != 0 and numFlag == True:
                ans += 1
                numFlag = False
            if h[j] > 0:
                h[j] -= 1

print(ans)
