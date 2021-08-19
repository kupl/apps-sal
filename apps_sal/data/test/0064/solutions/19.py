(n, k) = list(map(int, input().split()))
s = list(input())
cnt = {}
for c in s:
    if c in cnt:
        cnt[c] += 1
    else:
        cnt[c] = 1
ans = 'YES'
for v in list(cnt.values()):
    if k < v:
        ans = 'NO'
        break
print(ans)
