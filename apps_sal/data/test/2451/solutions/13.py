(n, h, a, b, k) = map(int, input().split())
while k:
    k -= 1
    (ta, fa, tb, fb) = map(int, input().split())
    ans = 0
    if ta == tb:
        print(abs(fa - fb))
        continue
    if fa < a:
        ans += a - fa
        ans += abs(fb - a)
    elif fa > b:
        ans += fa - b
        ans += abs(fb - b)
    else:
        ans += abs(fa - fb)
    ans += abs(ta - tb)
    print(ans)
