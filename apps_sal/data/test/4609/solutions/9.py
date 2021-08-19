from collections import Counter
n = int(input())
ans = 0
C = Counter((int(input()) for _ in range(n)))
for c in list(C.values()):
    if c % 2 == 1:
        ans += 1
print(ans)
