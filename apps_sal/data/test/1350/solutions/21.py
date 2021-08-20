(n, k) = list(map(int, input().split()))
s = input()
cnt = {k: 0 for k in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:k]}
for c in s:
    cnt[c] += 1
v = n
for c in cnt:
    v = min(v, cnt[c])
print(v * k)
