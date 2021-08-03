t = int(input())
for pp in range(0, t):
    n = int(input())
    ip = list(map(int, input().split()))
    if(ip[0] > 0):
        arr = []
        curr = ip[0]
        sign = 1
        for i in range(1, len(ip)):
            num = ip[i]
            if(num > 0 and sign == 1 and num > curr):
                curr = num
            elif(num < 0 and sign == 1):
                arr.append(curr)
                curr = num
                sign = -1
            elif(sign == -1):
                if(num < 0 and num > curr):
                    curr = num
                if(num > 0):
                    arr.append(curr)
                    curr = num
                    sign = 1
        arr.append(curr)
    else:
        arr = []
        curr = ip[0]
        sign = -1
        for i in range(1, len(ip)):
            num = ip[i]
            if(num > 0 and sign == 1 and num > curr):
                curr = num
            elif(num < 0 and sign == 1):
                arr.append(curr)
                curr = num
                sign = -1
            elif(sign == -1):
                if(num < 0 and num > curr):
                    curr = num
                if(num > 0):
                    arr.append(curr)
                    curr = num
                    sign = 1
        arr.append(curr)
    ss = sum(arr)
    print(ss)
