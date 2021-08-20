def gns():
    return list(map(int, input().split()))


n = int(input())
ns = gns()
cnt = [0] * 100
ans = 0
for c in ns:
    for l in range(100):
        if c % (1 << l) == 0:
            continue
        else:
            break
    l -= 1
    cnt[l] += 1
m = max(cnt)
for i in range(100):
    if cnt[i] == m:
        m = i
        break
x = []
for c in ns:
    if c % (1 << m) == 0 and c % (1 << m + 1) != 0:
        continue
    x.append(c)
print(len(x))
print(' '.join(map(str, x)))
