n = int(input())
a = list(map(int, input().split()))
b = [0] * n
for i in range(n):
    b[i] = a[i] - i
b.sort()
x = b[n // 2]
ans = 0
for i in range(n):
    ans += abs(b[i] - x)
print(ans)
