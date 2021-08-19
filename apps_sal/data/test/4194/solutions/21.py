(n, m) = list(map(int, input().split()))
l = list(map(int, input().split()))
left = n - sum(l)
if left < 0:
    print(-1)
else:
    print(left)
