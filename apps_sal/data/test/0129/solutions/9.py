(n, m, k, l) = list(map(int, input().split()))
required = k + l
per_friend = (required + m - 1) // m
if m * per_friend > n:
    print(-1)
else:
    print(per_friend)
