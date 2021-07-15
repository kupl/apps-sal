n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = None
topBottom = sum(a2)
for i in range(n):
    bottomTop = sum(a2)
    for j in range(n):
        if j != i:
            cur = topBottom + b[i] + bottomTop + b[j]
            ans = cur if ans == None else min(ans, cur)
        if (j < n - 1):
            bottomTop = bottomTop + a1[j] - a2[j]
    if i < n - 1:
        topBottom = topBottom + a1[i] - a2[i]
print(ans)

