def add(x):
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0]
for i in range(n):
    b.append((b[-1] + a[i] - 1) % k)
dic = {}
ans = 0
for i in range(n + 1):
    add(b[i])
    ans += dic[b[i]] - 1
    if i - k + 1 >= 0:
        dic[b[i - k + 1]] -= 1
print(ans)
