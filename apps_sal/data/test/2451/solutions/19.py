n, h, a, b, k = list(map(int, input().split()))
for i in range(k):
    fa, ta, fb, tb = list(map(int, input().split()))
    if (ta > tb):
        ta, tb = tb, ta
    if (fa == fb and ta == tb):
        print(0)
        continue
    
    ans = abs(fa - fb)
    
    if fa == fb:
        ans += abs(ta - tb)
    elif (ta > b):
        ans += abs(ta - b) + abs(b - tb)
    elif (tb < a):
        ans += abs(a - tb) + abs(a - ta)
    else:
        ans += abs(ta - tb)
    print(ans)

