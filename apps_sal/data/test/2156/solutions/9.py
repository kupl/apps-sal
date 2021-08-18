n = int(input())
a = list(map(int, input().split()))
s = [0 for _ in range(n + 1)]
s[1] = a[0]
for i in range(1, n):
    s[i + 1] = s[i] + a[i]
m = int(input())
for _ in range(m):
    x, y = list(map(int, input().split()))
    z = s[y] - s[x - 1]
    print(z // 10)
