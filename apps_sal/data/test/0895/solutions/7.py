n = int(input())
p = list(map(int, input().split()))
t = int(input())
p.sort()
ans = 0
i = 0
for j in range(n):
    while p[j] - p[i] > t:
        i = i + 1
    ans = max(ans, j - i + 1)
print(ans)
