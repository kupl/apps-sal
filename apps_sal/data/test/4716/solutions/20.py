N, K = map(int, input().split())
l = [int(l_) for l_ in input().split()]
l.sort(reverse=True)
print(sum(l[0:K]))
