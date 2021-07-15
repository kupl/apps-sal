T = int(input())
while T > 0:
    n = int(input())
    households = list(map(int, input().split()))
    stations = list(map(int, input().split()))
    l, r = 0, min(households[0],stations[0])
    ans = False
    while l <= r:
        mid = (l+r)//2
        left = households[0]-mid
        now = stations[0]-mid
        short = False
        for i in range(1,n):
            now = min(now, households[i])
            if now+stations[i] < households[i]:
                r = mid-1
                short = True
                break
            now = now+stations[i]-households[i]
        if short is True:
            continue
        if now >= left:
            ans = True
            break
        l = mid+1
    if ans:
        print('YES')
    else:
        print('NO')

    T -= 1
