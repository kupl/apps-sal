n, k = list(map(int, input().split()))
s = list(input())

s = list(sorted(s))
prv = 'Y'
cnt = 0
ans = 0
for c in s:
    if ord(prv) + 1 < ord(c):
        ans += ord(c) - ord('a') + 1
        prv = c
        cnt += 1
    if cnt == k:
        break

if cnt == k:
    print(ans)
else:
    print(-1)
