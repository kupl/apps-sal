(N, K) = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
l_max3 = l[0:K]
print(sum(l_max3))
