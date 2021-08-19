n = int(input())
a = list(map(int, input().split()))

a_even = a[0::2]
a_odd = a[1::2]

# even
if (n - 1) % 2 == 0:  # 0-(n-1)の実施なので(n-1)の偶奇を判定
    b = a_even.copy()
    b.reverse()
    b = b + a_odd
# odd
else:
    b = a_odd.copy()
    b.reverse()
    b = b + a_even

b = list(map(str, b))
print(' '.join(b))
