n = int(input())
argList = [int(input()) for _ in range(n)]
argList.sort()
ret = sum(argList)
if ret % 10 == 0:
    bias = 0
    for b in argList:
        if b % 10 != 0:
            bias = b
            break
    if bias == 0:
        print(0)
    else:
        print(ret - bias)
else:
    print(ret)
