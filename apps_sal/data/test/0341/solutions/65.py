(n, k) = map(int, input().split())
(r, s, p) = map(int, input().split())
t = input()
ans = 0
for i in range(k):
    R = 0
    S = 0
    P = 0
    cnt = 0
    while i + cnt * k < n:
        if i + cnt * k - k < 0:
            if t[i + cnt * k] == 'r':
                ans += p
                P = 1
            elif t[i + cnt * k] == 's':
                ans += r
                R = 1
            else:
                ans += s
                S = 1
        elif i + cnt * k - k >= 0 and t[i + cnt * k] == t[i + cnt * k - k]:
            if t[i + cnt * k] == 'r' and P == 0:
                ans += p
                P = 1
            elif t[i + cnt * k] == 'r' and P == 1:
                P = 0
            elif t[i + cnt * k] == 's' and R == 0:
                ans += r
                R = 1
            elif t[i + cnt * k] == 's' and R == 1:
                R = 0
            elif t[i + cnt * k] == 'p' and S == 0:
                ans += s
                S = 1
            elif t[i + cnt * k] == 'p' and S == 1:
                S = 0
        elif i + cnt * k - k >= 0 and t[i + cnt * k] != t[i + cnt * k - k]:
            if t[i + cnt * k] == 'r':
                ans += p
                P = 1
            elif t[i + cnt * k] == 's':
                ans += r
                R = 1
            else:
                ans += s
                S = 1
        cnt += 1
print(ans)
