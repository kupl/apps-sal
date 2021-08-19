(n, h, a, b, k) = map(int, input().split())
for i in range(k):
    (ta, fa, tb, fb) = map(int, input().split())
    if ta == tb:
        print(abs(fa - fb))
        continue
    ans = abs(ta - tb)
    if a <= fa <= b:
        first = fa
    elif abs(fa - a) < abs(fa - b):
        first = a
        ans += abs(fa - a)
    else:
        first = b
        ans += abs(fa - b)
    ans += abs(fb - first)
    print(ans)
