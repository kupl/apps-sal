N, K = map(int, input().split())
i = 0
while N != 0:
    N //= K
    i += 1
print(i)
