t = int(input())
for _ in range(t):
    n = int(input())
    arr = [[int(i) for i in input().split()] + [i] for i in range(n)]
    timearr = [0 for i in range(n)]
    checked = 0
    currtime = 1
    arr.sort(key=lambda a: a[0])
    while checked < n:
        if arr[checked][0] > currtime:
            currtime += 1
        elif arr[checked][1] < currtime:
            checked += 1
        else:
            timearr[arr[checked][2]] = currtime
            currtime += 1
            checked += 1
    print(' '.join(str(i) for i in timearr))
