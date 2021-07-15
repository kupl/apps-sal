n, h, a, b, k = map(int, input().split())
for i in range(k):
    ta, fa, tb, fb = map(int, input().split())
    if (ta == tb):
        ans = abs(fa - fb)
    elif (fa < a and fb < a):
        ans = (a - fa) + (a - fb) + abs(ta - tb)
    elif (fa > b and fb > b):
        ans = (fa - b) + (fb - b) + abs(ta - tb)
    else:
        ans = abs(fa - fb) + abs(ta - tb)
    print(ans)
