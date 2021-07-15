s = input().split()
n, k = (int(i) for i in s)
cnt1 = n - (n // 2)
if k <= cnt1:
    print(-1 + k * 2)
else:
    k -= cnt1
    print(k * 2)
