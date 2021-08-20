(n, m) = list(map(int, input().split()))
Min = (n + 1) // 2
while Min <= n and Min % m != 0:
    Min += 1
if Min <= n:
    print(Min)
else:
    print(-1)
