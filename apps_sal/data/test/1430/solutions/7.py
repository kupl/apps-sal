(N, K) = map(int, input().split())
S = [int(i) for i in input()]
(ans, r, l, k) = (0, 0, 0, K)
while r < N:
    while k > 0:
        while l < N and S[l] == 1:
            l += 1
        while l < N and S[l] == 0:
            l += 1
        k -= 1
    while l < N and S[l] == 1:
        l += 1
    ans = max(ans, l - r)
    while r < N and S[r] == 1:
        r += 1
    while r < N and S[r] == 0:
        r += 1
    k = 1
print(ans)
