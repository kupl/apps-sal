n, k = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
c = [a[i] - b[i] for i in range(n)]
ans = sum(b)
c.sort()
ans += sum(c[:k])
i = k
while i < n and c[i] < 0:
    ans += c[i]
    i += 1
print(ans)
