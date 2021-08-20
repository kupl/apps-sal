n = int(input())
a = list(map(int, input().split()))
ans = []
m = 0
for i in range(n - 1, -1, -1):
    ans.append(max(0, m + 1 - a[i]))
    m = max(m, a[i])
ans.reverse()
for i in ans:
    print(i, end=' ')
