n = int(input())
a = sorted(map(int, input().split()))
ans = 1
for i in range(n):
    if a[i] >= ans:
        ans += 1
print(ans)
