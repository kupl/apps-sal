for _ in range(int(input())):
    s, k = list(map(str, input().split()))
    k = int(k)
    su = 0
    for i in range(len(s)):
        su += int(s[i])
        if su >= k:
            ans = int(s[i:])
            ans = int("1" + (len(s) - i) * "0") - ans
            break
    su = 0
    for i in range(len(s)):
        su += int(s[i])
    if su <= k:
        print(0)
    else:
        print(ans)
