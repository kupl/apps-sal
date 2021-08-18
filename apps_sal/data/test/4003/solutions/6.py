n = int(input())
arr = list(map(int, input().split()))
i = 0
j = n - 1
ans = ''
prev = 0
while(i < j):
    if(arr[i] < arr[j]):
        if(arr[i] > prev):
            ans += 'L'
            prev = arr[i]
            i += 1
        elif(arr[j] > prev):
            ans += 'R'
            prev = arr[j]
            j -= 1
        else:
            break
    elif(arr[i] > arr[j]):
        if(arr[j] > prev):
            ans += 'R'
            prev = arr[j]
            j -= 1
        elif(arr[i] > prev):
            ans += 'L'
            prev = arr[i]
            i += 1
        else:
            break
    else:
        if(arr[i] < prev):
            break
        else:
            count1 = 0
            count2 = 0
            temp = i
            temprev = prev
            while(temp < j):
                if(arr[temp] > temprev):
                    temprev = arr[temp]
                    count1 += 1
                    temp += 1
                else:
                    break
            temp = j
            temprev2 = prev
            while(temp > i):
                if(arr[temp] > temprev2):
                    temprev2 = arr[temp]
                    count2 += 1
                    temp -= 1
                else:
                    break
            if(count1 >= count2):
                ans += 'L' * count1
                i += count1
                prev = temprev
            elif(count2 > count1):
                ans += 'R' * count2
                j -= count2
                prev = temprev2
            break

if(i == j and arr[i] > prev):
    ans += 'R'
    prev = arr[i]
print(len(ans))
print(ans)
