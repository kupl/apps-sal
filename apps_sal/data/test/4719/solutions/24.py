from collections import Counter
n = int(input())
a2z = 'abcdefghijklmnopqrstuvwxyz'
C = Counter(input())
for _ in range(1, n):
    c = Counter(input())
    for i in a2z:
        C[i] = min(C[i], c[i])
ans = ''
for (k, v) in sorted(C.items()):
    ans += k * v
print(ans)
