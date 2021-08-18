n, k = map(int, input().split())
S = list(map(int, list(input())))
ridx = 1
cnt = 0 if S[0] == 1 else 1
ans = 0
for lidx in range(n):
    if lidx > 0 and S[lidx] == 1 and S[lidx - 1] == 0:
        cnt -= 1
    while ridx < n:
        if S[ridx] == 0 and S[ridx - 1] == 1:
            if cnt < k:
                cnt += 1
            else:
                break
        ridx += 1
    ans = max(ans, ridx - lidx)
print(ans)
