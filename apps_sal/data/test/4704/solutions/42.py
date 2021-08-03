n = int(input())
a = [int(i) for i in input().split()]

sunuke = 0
araiguma = sum(a)

min_sa = 100000000000000

for i in range(n - 1):
    sunuke += a[i]
    araiguma -= a[i]
    min_sa = min(min_sa, abs(araiguma - sunuke))
print(min_sa)
