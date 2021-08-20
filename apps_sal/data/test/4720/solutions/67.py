N = int(input())
res = 0
for _ in range(N):
    (l, r) = list(map(int, input().split()))
    res += r - l + 1
print(res)
