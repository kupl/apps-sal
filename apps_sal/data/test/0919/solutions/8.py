(n, k) = map(int, input().split())
a = list(input())
a.sort()
c = ord('a') - 1
a = [ord(elem) - c for elem in a]
cur = -1
ans = 0
for i in range(n):
    if k == 0:
        break
    if a[i] > cur + 1:
        cur = a[i]
        ans += a[i]
        k -= 1
if k > 0:
    print(-1)
else:
    print(ans)
