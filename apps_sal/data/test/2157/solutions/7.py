(n, q) = map(int, input().split())
arr = list(map(int, input().split()))
pref = [0 for _ in range(n)]
for _ in range(q):
    (l, r) = map(int, input().split())
    pref[l - 1] += 1
    if r < n:
        pref[r] -= 1
lol = []
cur = 0
for i in range(n):
    cur += pref[i]
    lol.append(cur)
lol.sort()
arr.sort()
ans = 0
for i in range(n - 1, -1, -1):
    ans += arr[i] * lol[i]
print(ans)
