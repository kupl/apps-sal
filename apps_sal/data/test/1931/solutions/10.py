def generatepyramids():
    start = 2
    total = 2
    pyramids = [0, 2]
    for i in range(40000):
        start += 3
        total += start
        pyramids.append(total)
    return pyramids

def largestpyramid(n, pyramids):
    lo = 0
    hi = len(pyramids)
    mid = (lo + hi) // 2
    while lo != hi:
        mid = (lo + hi) // 2
        cur_pyramid = pyramids[mid]
        if cur_pyramid <= n:
            lo = mid + 1
        else:
            hi = mid
    if cur_pyramid <= n:
        return pyramids[mid]
    else:
        return pyramids[mid-1]

pyramids = generatepyramids()
t = int(input())
for case in range(t):
    n = int(input())
    answer = 0
    while n > 1:
        cur = largestpyramid(n, pyramids)
        n -= cur
        answer += 1
    print (answer)
        

    

