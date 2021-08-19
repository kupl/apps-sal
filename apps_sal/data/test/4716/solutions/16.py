(N, K) = map(int, input().split())
l = list(map(int, input().split()))
l_sorted = sorted(l, reverse=True)
total = 0
for i in range(K):
    total += l_sorted[i]
print(total)
