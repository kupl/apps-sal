(n, k) = list(map(int, input().split()))
hs = [int(input()) for i in range(n)]
hs = sorted(hs)
diff = 10 ** 12
for i in range(n - k + 1):
    diff = min(diff, hs[i + k - 1] - hs[i])
print(diff)
