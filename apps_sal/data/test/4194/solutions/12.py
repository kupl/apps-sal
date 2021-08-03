n, m = list(map(int, input().split()))
a = [int(x) for x in input().split()]
ans = n - sum(a)
print((str(max(ans, -1))))
