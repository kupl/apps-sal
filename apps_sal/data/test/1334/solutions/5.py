(n, k) = list(map(int, input().split()))
s = input()
S = set(s)
if n >= k:
    for i in reversed(list(range(k))):
        L = [q for q in S if s[i] < q]
        L = list(L)
        if len(L):
            print(s[:i] + min(L) + (k - i - 1) * min(S))
            break
else:
    print(s + min(S) * (k - n))
