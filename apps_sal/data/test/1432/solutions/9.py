n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    if i % 2 == 0:
        ans += a[i]
    else:
        ans -= a[i]
ans1 = ans
print(ans, end=' ')
for i in range(1, n):
    ans *= -1
    ans += 2 * a[i - 1]
    print(ans, end=' ')
print()
