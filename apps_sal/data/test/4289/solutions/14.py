n = int(input())
(t, a) = map(int, input().split())
h = list(map(int, input().split()))
ans = 0
temp = 1000000000000
for i in range(n):
    if temp > abs(a * 1000 - 1000 * t + h[i] * 6):
        temp = abs(a * 1000 - 1000 * t + h[i] * 6)
        ans = i + 1
print(ans)
