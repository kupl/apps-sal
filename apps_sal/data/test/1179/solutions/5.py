(n, k) = list(map(int, input().split()))
l = [0] + list(map(int, input().split()))
m = 0
for i in range(1, n + 1):
    if i * (i + 1) < k + k:
        m = i
    else:
        break
print(l[k - (m * (m + 1) >> 1)])
