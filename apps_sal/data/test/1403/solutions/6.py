from collections import Counter

n, K = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort()
C = Counter(a)

ans = n
s = sorted(C.keys())
for i, el in enumerate(s[1:]):
    if el - s[i] <= K:
        ans -= C[s[i]]

print(ans)

