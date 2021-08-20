n = int(input())
s = [list(map(int, input().split())) for i in range(n)]
stand = [0, 0]
prev = 0
for (t, x, y) in s:
    diff = abs(x + y - sum(stand))
    walk = t - prev
    if diff <= walk and walk % 2 == diff % 2:
        stand = [x, y]
        prev = t
    else:
        print('No')
        break
else:
    print('Yes')
