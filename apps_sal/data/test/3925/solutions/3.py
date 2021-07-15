def max_zebra(str):
    res=1
    cur=1
    for i in range(1,len(str)):
        if str[i] != str[i-1]:
            cur +=1
        else:
            if res < cur:
                res = cur
            cur = 1
    if res < cur:
        res = cur
    return res
    
str = input()
res = max_zebra(str+str)
if res > len(str):
    print(len(str))
else:
    print(res)
