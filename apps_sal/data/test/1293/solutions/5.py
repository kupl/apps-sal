n = int(input())
ans = 0
a = [0] + list(map(int, input().split()))
for i in range(n):
    ans += abs(a[i + 1] - a[i])
print(ans)
