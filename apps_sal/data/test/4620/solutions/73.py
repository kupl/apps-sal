N = int(input())
csf = [list(map(int, input().split())) for i in range(N - 1)]

for i in range(N):
    ans = 0
    for c, s, f in csf[i::]:
        if ans <= s:
            ans = s
        else:
            if ans % f == 0:
                pass
            else:
                ans = (ans // f + 1) * f
        ans += c
    print(ans)
