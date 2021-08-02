n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = [0] * n
for i in range(n // 2):
    ans[1 + i * 2] = a[i]
for i in range(n // 2, n):
    ans[(i - n // 2) * 2] = a[i]
co = 0
for i in range(1, n - 1):
    if ans[i - 1] > ans[i] and ans[i] < ans[i + 1]: co += 1
print(co)
print(*ans)
