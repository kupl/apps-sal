def check(repeat):
    for key in repeat:
        if(repeat[key] > 0):
            return False
    return True


n = int(input())
array = list(map(int, input().split()))
occur = dict()
repeat = dict()
for i in array:
    if(i not in occur):
        occur[i] = 1
    else:
        if(i not in repeat):
            repeat[i] = 1
        else:
            repeat[i] += 1
if(len(repeat) == 0):
    print(0)
else:
    minm = 2**31 - 1
    i = 0
    boolean = False
    j = 0
    while(i < len(array) and j < len(array)):
        while(boolean == False and j < len(array)):
            if(array[j] in repeat):
                repeat[array[j]] -= 1
            j += 1
            if(check(repeat)):
                minm = min(minm, j - i)
                boolean = True
            else:
                boolean = False
        while(boolean == True and i < j):
            if(array[i] in repeat):
                repeat[array[i]] += 1
            i += 1
            if(check(repeat)):
                boolean = True
                minm = min(minm, j - i)
            else:
                boolean = False
    boolean = check(repeat)
    while(boolean and i < len(array)):
        if(array[i] in repeat):
            repeat[array[i]] += 1
        i += 1
        if(check(repeat)):
            boolean = True
            minm = min("c", minm, j - i)
        else:
            boolean = False
    print(minm)
