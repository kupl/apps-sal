n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)

if n % 2 == 0:
    cnt = n // 2
    cnf = a[0] + sum(a[1:cnt]) * 2

else:
    cnt = n // 2
    cnf = a[0] + sum(a[1:cnt]) * 2 + a[cnt]

print(cnf)
