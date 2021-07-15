from collections import Counter

bad = False

n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

counts_a = Counter(A)
counts_b = Counter(B)
counts_total = Counter(A+B)

swaps = 0

for i in range(1,6):
    if counts_total[i] % 2 != 0:
        bad = True

    swaps += max(counts_a[i], counts_b[i]) - counts_total[i]//2

if bad:
    print(-1)
else:
    print(swaps//2)

