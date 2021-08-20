(n, k) = map(int, input().split())
if k % 2 == 0:
    cnt1 = n // k
    cnt2 = n // k
    if n % k >= k // 2:
        cnt2 += 1
    print(cnt1 ** 3 + cnt2 ** 3)
else:
    print((n // k) ** 3)
