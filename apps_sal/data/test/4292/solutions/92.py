N, K = (int(x) for x in input().split())
p = list(map(int, input().split()))
p.sort()
print(sum(p[:K]))
