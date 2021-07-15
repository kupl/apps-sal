n = int(input())
a = list(map(int, input().split()))
ans = 0
cnt = 0
for i in range(0, n, 2):
    cnt += a[i]
ans = cnt
j = 0
for i in range(n):
    cnt -= a[j % n]
    cnt += a[(j + 1) % n]
    ans = max(cnt, ans)
    j += 2
print(ans)
