''' بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ '''
# codeforces1207A_live
def gi(): return list(map(int, input().split()))


for k in range(gi()[0]):
    b, p, f = gi()
    h, c = gi()
    ans = 0
    if h > c:
        tmep = min(b // 2, p)
        ans += tmep * h
        b -= tmep * 2
        ans += min(b // 2, f) * c
    else:
        tmep = min(b // 2, f)
        ans += tmep * c
        b -= tmep * 2
        ans += min(b // 2, p) * h
    print(ans)
