n, k = list(map(int, input().split()))
l = list(map(int, input().split()))

L = sorted(l)

print((sum(L[(n - k):])))
