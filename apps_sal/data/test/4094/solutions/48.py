K = int(input())
ans = -1
r = 7 % K
SUM = r
if SUM % K == 0:
    ans = 1
else:
    for i in range(1, K):
        r = r * 10 % K
        SUM += r
        if SUM % K == 0:
            ans = i + 1
            break
print(ans)
