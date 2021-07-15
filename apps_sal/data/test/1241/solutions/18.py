n, k = map(int, input().split())
l = list(map(int, input().split()))
cnt = i = sm = 0
pos = 1
for j in range(n):
    sm += (l[j] == 0)
    while sm > k:
        sm -= (l[i] == 0)
        i += 1
    if j - i > cnt - pos:
        pos, cnt = i, j
print(cnt - pos + 1)
l[pos: cnt + 1] = [1] * (cnt - pos + 1)
print(' '.join(map(str, l)))
