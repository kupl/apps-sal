(n, k) = list(map(int, input().split()))
L = list(map(int, input().split()))
print(sum(sorted(L, reverse=True)[:k]))
