n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    if 2 * a[i] >= b[i] and b[i] > 1:
        x = b[i] // 2
        ans += (x * (b[i] - x))
    else:
        ans -= 1
print(ans)
