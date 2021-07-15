ans = 0
n = int(input())
a = list(map(int, input().split())) + [0]
for i in range(n):
    ans += abs(a[i] - a[i - 1])
print(ans)

