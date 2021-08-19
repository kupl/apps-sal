(n, m, d) = list(map(int, input().split()))
lis = list(map(int, input().split()))
l1 = [[lis[i], i] for i in range(n)]
l1.sort()
ans = [0] * n
j = k = 0
for i in range(n):
    if l1[i][0] - l1[j][0] <= d:
        k += 1
        ans[l1[i][1]] = k
    else:
        ans[l1[i][1]] = ans[l1[j][1]]
        j += 1
print(k)
print(*ans)
