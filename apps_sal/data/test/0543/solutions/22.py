def I(): return list(map(int, input().split()))


n, a = I()[0], I()
active_coupon = False
for i in range(n):
    q = a[i] - 1 * active_coupon
    if q >= 0:
        r = q % 2
        active_coupon = [True, False][r != 1]
    else:
        active_coupon = True
        break
print('YNEOS'[active_coupon::2])
