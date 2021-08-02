n, k = map(int, input().split())
x = [int(i) for i in input().split()]
ans = 10**9

for i in range(n - k + 1):
    temp = 0
    temp += (min(abs(x[i]), abs(x[i + k - 1])) + abs(x[i] - x[i + k - 1]))
    ans = min(ans, temp)
print(ans)
