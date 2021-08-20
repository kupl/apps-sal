import itertools
n = int(input())
A = [int(i) for i in input().split()]
A_sum = [0] + list(itertools.accumulate(A))
'累積和は単調増加\n4パートに分ければいいので別ける箇所3点left,mid,rightを探す．\n全探索はTLEなのでmidに関するループ探索を行うと，条件式からl,rは決まる．\n今回の問題では差をなくすことが目的なので，0~l,l~iとi~r,r~nの差が小さい時がベスト\nこの条件のもと，lとrを決める．for文で書く場合break入れないとTLE\n\n'
ans = 10 ** 9
(P, Q, R, S) = (0, 0, 0, 0)
l = 0
r = 2
for i in range(1, n):
    while l < i and abs(A_sum[l] - (A_sum[i] - A_sum[l])) >= abs(A_sum[l + 1] - (A_sum[i] - A_sum[l + 1])):
        l += 1
    while r < n and abs(A_sum[n] - A_sum[r] - (A_sum[r] - A_sum[i])) >= abs(A_sum[n] - A_sum[r + 1] - (A_sum[r + 1] - A_sum[i])):
        r += 1
    P = A_sum[l]
    Q = A_sum[i] - P
    R = A_sum[r] - A_sum[i]
    S = A_sum[n] - A_sum[r]
    ans = min(ans, abs(max(P, Q, R, S) - min(P, Q, R, S)))
print(ans)
