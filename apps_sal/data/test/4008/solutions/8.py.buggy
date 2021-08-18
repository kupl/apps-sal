n, k = list(map(int, input().split()))
a = [int(e) for e in input().split()]
b = [1] * 5555
cnt = [0] * 5555
c = []
for i in a:
    if b[i] > k:
        print('NO')
        return
    c.append(b[i])
    cnt[b[i]] += 1
    b[i] += 1
for i in range(1, k + 1):
    if cnt[i] > 0:
        continue
    for k, j in enumerate(c):
        if cnt[j] > 1:
            c[k] = i
            cnt[j] -= 1
            break

print('YES')
print(' '.join(str(e) for e in c))
