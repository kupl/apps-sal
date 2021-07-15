N, K = list(map(int, input().split()))
ps = list(map(int, input().split()))
print((sum(sorted(ps)[:K])))

