n = int(input())
l = [int(x) for x in input().split()]
ans = 0
for i in range(1, n - 1):
    if l[i - 1] < l[i] < l[i + 1] or l[i - 1] > l[i] > l[i + 1]:
        ans += 1
print(ans)
