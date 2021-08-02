n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(max(a)):
    cnt = 1 if a[0] - i >= 1 else 0
    for j in range(1, n):
        if a[j - 1] - i < 1 and a[j] - i >= 1:
            cnt += 1
    ans += cnt
print(ans)
