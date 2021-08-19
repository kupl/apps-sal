k = int(input())
n = 50
(x, y) = divmod(k, n)
ans = [i + x for i in range(n)]
for i in range(y):
    i %= n
    ans[i] += n
    for j in range(n):
        if i == j:
            continue
        ans[j] -= 1
print(n)
print(*ans)
