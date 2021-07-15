from collections import Counter
N = int(input())
S = input()
ans = 0
for i in range(N):
    d1 = Counter(S[:i])
    d2 = Counter(S[i:])
    tmp = 0
    for alphabet in 'abcdefghijklmnopqrstuvwxyz':
        tmp += min(d1[alphabet], d2[alphabet], 1)
    print
    ans = max(ans, tmp)
print(ans)
