n = int(input())
l = list(map(int, input().split()))
ans = 0
l.sort()
for i in range(n // 2):
    ans += (l[i] + l[n - i - 1])**2
print(ans)
