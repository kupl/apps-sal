n = int(input())
x = list(map(int, input().split()))
x.sort()
ans = 0
for i in range(n):
    ans += (pow(2, i, 1000000007) - pow(2, n - i - 1, 1000000007)) * x[i] % 1000000007
    ans = ans % 1000000007
print(ans)
