n, m = list(map(int, input().split()))
l1 = list(map(int, input().split()))
ans = 0
for i in range(m):
    sum1 = 0
    l, r = list(map(int, input().split()))
    l -= 1
    r -= 1
    for j in range(l, r + 1):
        sum1 += l1[j]
    if sum1 > 0:
        ans += sum1
print(ans)
