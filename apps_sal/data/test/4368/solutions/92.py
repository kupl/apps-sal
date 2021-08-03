def base10toK_base(num, K):
    if num // K:
        return base10toK_base(num // K, K) + str(num % K)
    return str(num % K)


N, K = map(int, input().split())
ans = len(base10toK_base(N, K))
print(ans)
