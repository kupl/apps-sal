def d_no_need(N, K, A):
    card = sorted(A, reverse=True)
    s = 0
    ans = 0
    for a in card:
        if s + a < K:
            s += a
            ans += 1
        else:
            ans = 0
    return ans


(N, K) = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
print(d_no_need(N, K, A))
