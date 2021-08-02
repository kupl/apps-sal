n = int(input())
a = [0] * 1000
b = [0] * 1000
lst = [0] * 1001
for x in range(n):
    a[x], b[x] = map(int, input().split())
    lst[b[x]] += 1
ans = 0
for x in range(n):
    lst[b[x]] -= 1
    if lst[a[x]] == 0:
        ans += 1
    lst[b[x]] += 1
print(ans)
