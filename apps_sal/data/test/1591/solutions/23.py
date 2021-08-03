n, k = list(map(int, input().split()))
l = [0] * (k + 1)
for i in range(n):
    a = int(input())
    l[a] += 1
ans = 0
cnt = 0
for i in range(k + 1):
    ans += l[i]
    if (l[i] % 2 == 1):
        cnt += 1
        ans -= 1
print(ans + cnt // 2 + cnt % 2)
