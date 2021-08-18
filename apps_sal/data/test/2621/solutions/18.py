import math

t = int(input())
for i in range(t):
    possible = True
    n, m, k = list(map(int, input().split()))
    arr = input().split()
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    maxBlocks = m
    for j in range(1, n):
        if(arr[j] - arr[j - 1] > maxBlocks + k):
            possible = False
        else:
            if(arr[j - 1] >= arr[j] - k):
                maxBlocks += min(arr[j - 1] - max(arr[j] - k, 0), arr[j - 1])
            elif(arr[j - 1] < arr[j] - k):
                maxBlocks -= abs(arr[j] - arr[j - 1]) - k
    if(possible):
        print("YES")
    else:
        print("NO")
