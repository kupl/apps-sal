strs = input()
array = []
char = []
count = 1
char.append(strs[0])
i = 1
while(i < len(strs)):
    if(strs[i] == strs[i - 1]):
        count += 1
    else:
        array.append(count)
        char.append(strs[i])
        count = 1
    i += 1
array.append(count)
bback = []
aback = []
bfront = []
afront = []
i = 0
while(i < len(array)):
    if(i == 0):
        if(char[i] == 'b'):
            aback.append(0)
            bback.append(array[0])
        else:
            bback.append(0)
            aback.append(array[0])
    else:
        if(char[i] == 'b'):
            aback.append(aback[i - 1])
            bback.append(bback[i - 1] + array[i])
        else:
            aback.append(aback[i - 1] + array[i])
            bback.append(bback[i - 1])
    i += 1
i = 0
while(i < len(array)):
    afront.append(aback[-1] - aback[i])
    bfront.append(bback[-1] - bback[i])
    i += 1
if(len(array) == 1):
    print(array[0])
else:
    maxm = -1
    i = 0
    while(i < len(array)):
        if(char[i] == 'b'):
            j = i
            while(j < len(array)):
                if(char[j] == 'b'):
                    if(j == i):
                        ans = aback[i] + array[i] + afront[i]
                        if(ans > maxm):
                            maxm = ans
                    else:
                        ans = aback[i] + array[i] + (bback[j] - bback[i]) + afront[j]
                        if(ans > maxm):
                            maxm = ans
                j += 1
        i += 1
    print(maxm)
