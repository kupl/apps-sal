(N, K) = map(int, input().split())
ls = list(map(int, input().split()))
print(sum(sorted(ls, reverse=True)[:K]))
