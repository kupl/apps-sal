n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
if sum(a) + k >= n * 100:
    print(n * 10)
    return
adds = []
ans = 0
for i in range(n):
    ans += a[i] // 10
    if a[i] != 100:
        adds.append(10 - (a[i] % 10))
adds.sort()
for i in range(len(adds)):
    if k <= 0:
        break
    else:
        k -= adds[i]
        ans += 1
ans += k // 10
print(ans)

