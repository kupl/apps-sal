(n, k) = map(int, input().split())
hl = []
for i in range(n):
    hl.append(int(input()))
hl.sort()
ans = 10000000001
for j in range(n - k + 1):
    s = hl[j + k - 1] - hl[j]
    if s < ans:
        ans = s
    else:
        pass
print(ans)
