N, K = map(int, input().split())
V = list(map(int, input().split()))
W = V[::-1]
R = min(N, K)
ans = -float('inf')
for left in range(R+1):
    for right in range(R+1):
        if left+right > R: continue
        A = V[:left]+W[:right]
        tmp = sum(A)
        
        rest = K - left - right
        A = [k for k in A if k < 0]
        A.sort()
        if rest >= 0:
            tmp -= sum(A[:min(rest, len(A))])
        ans = max(tmp, ans)

print(ans)
