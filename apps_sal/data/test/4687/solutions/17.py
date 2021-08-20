(N, K) = [int(i) for i in input().split()]
(a, b) = ([], [])
for _ in range(N):
    tmp = input().split()
    a.append(int(tmp[0]))
    b.append(int(tmp[1]))
cnt = [0] * (100000 + 1)
for i in range(N):
    cnt[a[i]] += b[i]
for j in range(100000 + 1):
    if K <= cnt[j]:
        print(j)
        break
    K -= cnt[j]
