n, k = map(int, input().split())
a = list(map(int, input().split()))

acsum = [0]
for i in range(n):
    acsum.append(acsum[i] + a[i])

cnt =0
p = 0
for i in range(n + 1):
    if acsum[i] >= k:
        p = i
        break        

if acsum[n] < k:
    pass
else:
    j = 0
    for i in range(p, n + 1):
        while j <= i:
            if acsum[i] - acsum[j] >= k:
                j += 1
                continue
            else: # acsum[i] - acsum[j] < k
                cnt += j
                j = j - 1
                break
print(cnt)
