n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += min(b[i], a[i] + a[i + 1])
    n1 = min(a[i], b[i])
    b[i] -= n1
    a[i + 1] = max(0, a[i + 1] - b[i])
print(ans)
