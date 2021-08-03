n = int(input())
H = list(map(int, input().split()))
cnt = [0] * n

for i in reversed(list(range(1, n))):
    m = H[i]
    for j in range(0, i):
        if H[j] <= m:
            cnt[i] += 1
        else:
            break

ans = 0
for i in range(n):
    if cnt[i] == i:
        ans += 1
# print(cnt)
print(ans)
