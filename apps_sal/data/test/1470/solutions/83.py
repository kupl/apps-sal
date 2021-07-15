x = int(input())

if 0 <= x <= 6:
    print(1)
elif 6<x<12:
    print(2)
else:
    ans = x//11 * 2
    x = x%11
    #print(x)
    if x == 0:
        ans += 0
    elif 0<x<=6:
        ans += 1
    elif 6<x<12:
        ans += 2
    print(ans)
