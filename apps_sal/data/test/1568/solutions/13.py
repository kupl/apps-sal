n = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = 0
if n[2] >= n[3]:
    print(n[0] * n[1])
else:
    for i in t:
        if i == n[4]:
            ans += n[1]
        else:
            ans += n[1] + (n[4] - i) * (n[3] - n[2])
    print(ans)
