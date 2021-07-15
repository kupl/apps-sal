N, K = list(map(int, input().split()))
K = abs(K)

ans = 0
ab = 2*N
pat = 1
while ab - K >= 2:
    if ab-K >= (2+2*N)//2:
        ans += (pat + K)*pat
    else:
        ans += (ab - K - 2 + 1)*pat
    ab -= 1
    if ab  >= (2+2*N)//2:
        pat += 1
    else:
        pat -= 1
print(ans)



