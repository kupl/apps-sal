n, k = list(map(int, input().split()))

ans = [0] * k

a = list(map(int, input().split()))

for c in a:
    ans[c % k] += 1
kol = ans[0] - ans[0] % 2
for i in range(1, int(k / 2 + 0.5)):
    kol += min(ans[i], ans[k - i]) * 2
    #print(ans[i], ans[k - i], i)

if k % 2 == 0:
    kol += ans[k // 2] - ans[k // 2] % 2
# print(ans)
print(kol)
