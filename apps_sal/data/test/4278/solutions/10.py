from collections import Counter
N = int(input())
l = []
for i in range(N):
    s = input()
    S = [s[x] for x in range(10)]
    S = sorted(S)
    s = ''
    for j in range(10):
        s += S[j]
    l.append(s)
l = Counter(l)
c = l.values()
ans = 0
for i in c:
    ans += i * (i - 1) // 2
print(ans)
