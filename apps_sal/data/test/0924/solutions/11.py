la, ra, ta = list(map(int, input().split()))
lb, rb, tb = list(map(int, input().split()))
a, b = ta, tb
while b:
    a, b = b, a % b
ra -= la // a * a
la %= a
rb -= lb // a * a
lb %= a
print(max(min(ra, rb) + 1 - max(la, lb), min(ra + a, rb) + 1 - max(la + a, lb), min(ra, rb + a) + 1 - max(la, lb + a), 0))
