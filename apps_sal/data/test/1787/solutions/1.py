s = input()
lengths = []
cnt = 0
eps = 1e-8

for c in s:
    if c == 'b':
        if cnt > 0:
            lengths.append(cnt)
        cnt = 0
    elif c == 'a':
        cnt += 1
if cnt > 0:
    lengths.append(cnt)
    cnt = 0


ans = 1
for l in lengths:
    ans *= (l + 1)
    ans %= (1e9 + 7)
ans -= 1
print(int(ans % (1e9 + 7) + eps))
