k, n = map(int, input().split())
a = list(map(int, input().split()))

n = len(a) - 1
cnt = [a[n] - a[0]]
for i in range(n):
    cnt.append(k - (a[i + 1] - a[i]))
ans = min(cnt)

print(ans)
