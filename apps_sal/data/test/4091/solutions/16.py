(n, k) = map(int, input().split())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append((a[i], i))
b.sort(reverse=True)
sum = 0
lol = [-1]
for i in range(k):
    sum += b[i][0]
    lol.append(b[i][1])
lol.sort()
ans = []
for i in range(1, k + 1):
    ans.append(lol[i] - lol[i - 1])
ans[k - 1] += n - 1 - lol[k]
print(sum)
print(*ans)
