(N, K) = map(int, input().split())
l = list(map(int, input().split()))
new_l = sorted(l, reverse=True)
print(sum(new_l[0:K]))
