n, m = list(map(int, input().split()))

cs = [list(map(int, input().split())) for _ in range(m)]
ps = list(map(int, input().split()))

ans = 0
for on in range(2**n):
    patern = bin(on)[2:].rjust(n, '0')
    ok = True

    for i in range(m):
        ct = 0
        for j in range(cs[i][0]):
            if patern[cs[i][j + 1] - 1] == '1':
                ct += 1
        if ct % 2 != ps[i]:
            ok = False
    if ok:
        ans += 1
print(ans)
