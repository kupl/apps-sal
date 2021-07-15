from collections import Counter

N, P = list(map(int, input().split()))
S = input()

ans = 0

if not 10 % P:
    for r in range(N):
        if not int(S[r]) % P:
            ans += r+1
else:
    S = S[::-1]
    s = 0
    d = [0] * (N+1)
    
    for i in range(N):
        s = (s + int(S[i]) * pow(10, i, P)) % P
        d[i+1] = s

    c = Counter()
    for i in range(N+1):
        ans += c[d[i]]
        c[d[i]] += 1
              
print(ans)
