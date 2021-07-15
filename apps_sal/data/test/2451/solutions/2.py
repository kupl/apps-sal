n, h, a, b, k = list(map(int, input().strip().split()))

for i in range(k):
    ta, fa, tb, fb = list(map(int, input().strip().split()))
    ans = 0
    to = fa
    if (ta == tb):
        print(abs(fa - fb))
        continue
    if (fa > b):
        ans = fa - b
        to = b
    if (fa < a):
        ans = a - fa
        to = a
    ans += abs(tb - ta)
    ans += abs(fb - to)
    print(ans)

