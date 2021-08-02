n = int(input())
w = list(map(int, input().split()))
w.sort()
ans = 50000
for i in range(2 * n - 1):
    for j in range(i + 1, 2 * n):
        tmp = 0
        for k in range(2 * n):
            if k < i or j < k:
                if k % 2 == 0:
                    tmp -= w[k]
                else:
                    tmp += w[k]
            elif i < k < j:
                if k % 2 == 1:
                    tmp -= w[k]
                else:
                    tmp += w[k]
        ans = min(ans, tmp)
print(ans)
