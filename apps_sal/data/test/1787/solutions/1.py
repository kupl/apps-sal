s = input()
lengths = []
cnt = 0
eps = 1e-08
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
    ans *= l + 1
    ans %= 1000000000.0 + 7
ans -= 1
print(int(ans % (1000000000.0 + 7) + eps))
