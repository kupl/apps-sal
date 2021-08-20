t = int(input())
for _ in range(t):
    (n, x) = list(map(int, input().split()))
    b = [tuple(map(int, input().split())) for i in range(n)]
    shot_gun = b[0]
    uzi = b[0]
    for blow in b:
        if blow[0] > shot_gun[0]:
            shot_gun = blow
        if blow[0] - blow[1] > uzi[0] - uzi[1]:
            uzi = blow
    ans = None
    if shot_gun[0] >= x:
        ans = 1
    elif uzi[0] <= uzi[1]:
        ans = -1
    else:
        ans = 1 + (x - shot_gun[0] + uzi[0] - uzi[1] - 1) // (uzi[0] - uzi[1])
    print(ans)
