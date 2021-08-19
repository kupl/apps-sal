(N, K) = list(map(int, input().split()))
p = list(map(int, input().split()))
p = sorted(p)
print(sum(p[:K]))
