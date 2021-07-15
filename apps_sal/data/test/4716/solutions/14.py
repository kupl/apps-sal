N, K = list(map(int, input().split()))
print((sum(sorted(map(int, input().split()), reverse=True)[:K])))

