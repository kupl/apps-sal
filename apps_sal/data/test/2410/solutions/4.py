# = map(int, input().split())
# = list(map(int, input().split()))
t = int(input())
for _ in range(t):
    n = int(input())
    z = list(map(int, input().split()))
    sm = sum(z)
    maxsum = 0
    minpref = 0
    curpref = 0
    for a in z[:-1]:
        curpref += a
        if curpref - minpref > maxsum:
            maxsum = curpref - minpref
        minpref = min(minpref, curpref)
    minpref = 0
    curpref = 0
    for a in z[1:]:
        curpref += a
        if curpref - minpref > maxsum:
            maxsum = curpref - minpref
        minpref = min(minpref, curpref)
    if maxsum < sm:
        print('YES')
    else:
        print('NO')
