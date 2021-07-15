# a,b = list(map(int, input().strip().split()))
n = int(input())

a = list(map(int, input().strip().split()))

ena = a.count(1)
dva = a.count(2)

vseh = 0

m = min(ena,dva)

vseh += m
ena -= m
dva -= m

vseh += ena//3

print(vseh)

