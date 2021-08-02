q = int(input())
for _ in range(q):
    n, r = map(int, input().split())
    max_k = min(n - 1, r)
    wyn = max_k * (max_k + 1) // 2
    if r >= n:
        wyn += 1
    print(wyn)
