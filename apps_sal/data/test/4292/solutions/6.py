(n, k) = list(map(int, input().split()))
p = sorted(map(int, input().split()))
print(sum(p[:k]))
