N, K = [int(i) for i in input().split(' ')]
p = [int(i) for i in input().split(' ')]
p.sort()
print(sum(p[:K]))
