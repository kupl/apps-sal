def calc(arr, ll, a, b, x, y):
    # y is always greater than x
    rXY = 0
    rX = 0
    rY = 0
    result = 0
    for i in range(1, ll+1):
        if i % a == 0 and i % b == 0:
            rXY += 1
        elif i % a == 0:
            rX += 1
        elif i % b == 0:
            rY += 1
    for i in range(rXY):
        result += arr[i] * ((x + y)/100)
    for i in range(rX):
        result += arr[rXY + i] * (x/100)
    for i in range(rY):
        result += arr[rXY + rX + i] * (y/100)
    return result

q = int(input())
for _ in range(q):
    n = int(input())
    arr = list(map(int, input().split()))
    x, a = list(map(int, input().split()))
    y, b = list(map(int, input().split()))
    k = int(input())

    if x < y:
        x, y = y, x
        a, b = b, a

    arr.sort(reverse=True)
    
    left = 0
    right = n + 1
    while (right - left > 1): 
        mid = (right + left) // 2
        if calc(arr, mid, a, b, x, y) >= k:
            right = mid
        else:
            left = mid
            
    print(right if right <= n else -1)
