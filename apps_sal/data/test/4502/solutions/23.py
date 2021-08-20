n = int(input())
a = list(map(int, input().split()))
a_even = a[0::2]
a_odd = a[1::2]
if (n - 1) % 2 == 0:
    b = a_even.copy()
    b.reverse()
    b = b + a_odd
else:
    b = a_odd.copy()
    b.reverse()
    b = b + a_even
b = list(map(str, b))
print(' '.join(b))
