n, x = map(int, input().split())
m = [0] * n
for i in range(n):
    m[i] = int(input())
for i in range(n):
    x -= m[i]
m.sort()
ans = n + x // m[0]
print(ans)
