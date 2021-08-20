(N, K) = list(map(int, input().split()))
ab = list((list(map(int, input().split())) for _ in range(N)))
ab.sort()
i = 0
while K > 0:
    K -= ab[i][1]
    i += 1
print(ab[i - 1][0])
