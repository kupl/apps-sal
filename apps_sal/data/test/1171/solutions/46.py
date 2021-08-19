(N, K) = map(int, input().split())
V = list(map(int, input().split()))
ans = 0
for lg in range(K + 1):
    for rg in range(K - lg + 1):
        if lg + rg > N:
            break
        for ls in range(K - lg - rg + 1):
            if ls > lg:
                break
            for rs in range(K - lg - rg - ls + 1):
                if rs > rg:
                    break
                lv = V[:lg]
                rv = V[N - rg:]
                '\n                print(lg, ls, rg, rs)\n                print(lv, rv)\n                print(lv[:lg-ls], rv[:rg-rs])\n                print()\n                '
                lv.sort()
                lv.reverse()
                rv.sort()
                rv.reverse()
                ans = max(sum(lv[:lg - ls]) + sum(rv[:rg - rs]), ans)
print(ans)
