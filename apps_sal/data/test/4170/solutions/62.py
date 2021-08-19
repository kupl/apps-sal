n = int(input())
L = list(map(int, input().split()))
(ans, cnt, tmp) = (0, 0, L[0])
for i in range(1, n):
    if tmp >= L[i]:
        tmp = L[i]
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0
        tmp = L[i]
print(ans)
