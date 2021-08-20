(n, k) = map(int, input().split())
a = list(map(int, input().split()))
acsum = [0]
for i in range(n):
    acsum.append(acsum[i] + a[i])
cnt = 0
jj = 0
for i in range(n):
    for j in range(jj, n - i):
        if acsum[i + j + 1] - acsum[i] >= k:
            cnt += n - i - j
            jj = j - 1
            break
print(cnt)
