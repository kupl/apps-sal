n = int(input())
a = list(map(int, input().split()))
r = list(map(lambda x: x % 3, a))
memo = [0] * n
t = 0
for i in range(n):
    if i > 0:
        if memo[i - 1] * 2 <= a[i]:
            memo[i] = (a[i] - memo[i - 1] * 2) % 3
        else:
            memo[i] = memo[i - 1] - a[i] // 2 + a[i] % 2
    else:
        memo[i] = r[i]
print((sum(a) - memo[n - 1]) // 3)
