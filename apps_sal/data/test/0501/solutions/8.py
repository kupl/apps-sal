(l, r) = list(map(int, input().split()))
l -= 1
if l == 0:
    ar1 = []
else:
    ar1 = [1]
sum1 = 1
while sum1 < l:
    if sum1 + ar1[-1] * 2 <= l:
        sum1 += ar1[-1] * 2
        ar1.append(ar1[-1] * 2)
    else:
        ar1.append(l - sum1)
        sum1 = l
ar2 = [1]
sum2 = 1
while sum2 < r:
    if sum2 + ar2[-1] * 2 <= r:
        sum2 += ar2[-1] * 2
        ar2.append(ar2[-1] * 2)
    else:
        ar2.append(r - sum2)
        sum2 = r
sum1_odd = sum(ar1[::2])
sum1_even = sum(ar1[1::2])
sum2_odd = sum(ar2[::2])
sum2_even = sum(ar2[1::2])
p = 10 ** 9 + 7
print((sum2_odd ** 2 + sum2_even ** 2 + sum2_even - sum1_odd ** 2 - sum1_even ** 2 - sum1_even) % p)
