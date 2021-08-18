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
if(i == j and arr[i] > prev):
    ans += 'R'
    prev = arr[i]
print(len(ans))
print(ans)
