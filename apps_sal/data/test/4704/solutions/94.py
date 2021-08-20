n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
for i in range(1, n):
    b.append(b[-1] + a[i])
s = sum(a)
ans = 10 ** 20
for i in range(n - 1):
    ans = min(ans, abs(s - 2 * b[i]))
print(ans)
