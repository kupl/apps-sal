t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    s = list(input())
    s.sort()
    ans = []
    if k == n:
        print(s[k - 1])
    elif s[0] == s[k - 1] and s[k] == s[n - 1]:
        ans_s = s[0] + s[k] * ((n - k) // k)
        if n % k == 0:
            print(ans_s)
        else:
            print(ans_s + s[k])
    else:
        if s[0] == s[k - 1]:
            print(s[0] + "".join(list(map(str, s[k:]))))
        else:
            print(s[k - 1])
