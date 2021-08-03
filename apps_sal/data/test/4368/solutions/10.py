N, K = map(int, input().split())
i = 0
while N >= 1:
    N //= K
    i += 1
print(i)
