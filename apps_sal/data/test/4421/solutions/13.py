from collections import Counter
n, k = list(map(int, input().split()))
D = list(map(int, input().split()))

D2 = [d % k for d in D]

c = Counter(D2)

ANS = c[0] // 2 * 2
if k % 2 == 0:
    ANS += c[k // 2] // 2 * 2
for i in range(1, -(-k // 2)):
    ANS += min(c[i], c[k - i]) * 2

print(ANS)
