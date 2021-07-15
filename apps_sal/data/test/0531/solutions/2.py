n = int(input())
arr = list(map(int, input().split()))
mn = min(arr)
mx = max(arr)
if mn == mx:
    print(n)
    print(*arr)
elif mn + 1 == mx:
    print(n)
    print(*arr)
else:
    a = 0
    b = 0
    c = 0
    for i in range(n):
        if arr[i] == mn:
            a += 1
        elif arr[i] == mx:
            c += 1
        else:
            b += 1
    a1 = a + b // 2
    c1 = c + b // 2
    b1 = b % 2
    s1 = min(a1, a) + min(b1, b) + min(c1, c)
    b2 = b + min(a, c) * 2
    q = min(a, c)
    a2 = a - q
    c2 = c - q
    s2 = min(a2, a) + min(b2, b) + min(c2, c)
    if s1 < s2:
        print(s1)
        ans = [mn] * a1 + [mn + 1] * b1 + [mx] * c1
        print(*ans)
    else:
        print(s2)
        ans = [mn] * a2 + [mn + 1] * b2 + [mx] * c2
        print(*ans)



