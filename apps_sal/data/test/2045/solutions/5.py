def zalgo(S):
    L = len(S)
    Z = [0]*L
    l = 0
    for i in range(1, L):
        if i + Z[i-l] < l + Z[l]:
            Z[i] = Z[i-l]
        else:
            cnt = max(0, l+Z[l]-i)
            while i + cnt < L and S[i+cnt] == S[cnt]:
                cnt += 1
            Z[i] = cnt
            l = i
    Z[0] = L
    return Z

N = int(input())
S = [list(map(ord, s)) for s in input().strip().split()]             
Ans = [0]*(10**6)
for s in S:
    n = len(s)
    Z = zalgo(s+[-1]+Ans[-n:])[n+1:] + [0]
    for i in range(n+1):
        if n - i == Z[i]:
            Ans += s[n-i:]
            break
    
Ans = Ans[10**6:]
print(''.join(map(chr, Ans)))
