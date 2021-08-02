from collections import Counter
n = int(input())
A = sorted(map(int, input().split()))
m = A[-1]
C = Counter(A)
flags = [True for _ in range(m + 1)]
for a in A:
    if flags[a]:
        i = 2
        x = a * i
        while x <= m:
            flags[x] = False
            i += 1
            x = a * i
ans = 0
for a in set(A):
    if C[a] == 1 and flags[a]:
        ans += 1
print(ans)
