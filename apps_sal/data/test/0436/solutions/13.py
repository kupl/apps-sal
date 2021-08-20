n = int(input())
a = list(map(int, input().split()))
sum1 = sum(a)
sum2 = a[0]
ans = [1]
for i in range(1, n):
    if a[0] >= 2 * a[i]:
        sum2 += a[i]
        ans.append(i + 1)
if 2 * sum2 > sum1:
    print(len(ans))
    print(*ans)
else:
    print(0)
