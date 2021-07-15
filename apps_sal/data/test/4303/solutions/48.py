N, K = list(map(int, input().split()))
x = list(map(int, input().split()))

ans = []
for i in range(N - K + 1):
    left = i
    right = left + K - 1
    if x[left] < 0 and x[right] >= 0:
        q = min(abs(x[left]) * 2 + x[right], x[right] * 2 + abs(x[left]))
        ans.append(q)
        continue
    elif x[right] < 0:
        q = abs(x[left])
        ans.append(q)
        continue
    elif x[left] > 0:
        q = abs(x[right])
        ans.append(q)
        continue
if len(ans) == 0:
    print((0))
    return

print((min(ans)))

