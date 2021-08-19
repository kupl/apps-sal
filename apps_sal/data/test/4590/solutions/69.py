(n, m, k) = map(int, input().split())
shelfA = list(map(int, input().split()))
shelfB = list(map(int, input().split()))
prodA = [0] * (n + 1)
prodB = [0] * (m + 1)
for i in range(1, n + 1):
    prodA[i] = prodA[i - 1] + shelfA[i - 1]
for i in range(1, m + 1):
    prodB[i] = prodB[i - 1] + shelfB[i - 1]
ans = -1
j = m
for i in range(n + 1):
    if prodA[i] > k:
        break
    while prodB[j] > k - prodA[i]:
        j -= 1
    ans = max(ans, i + j)
print(ans)
