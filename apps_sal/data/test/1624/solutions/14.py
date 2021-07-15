n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n//2):
    ans += (a[i] + a[-1-i]) ** 2
print(ans)

