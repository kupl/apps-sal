
n = int(input())

m = n - 1
ii = 1
for i in range(1, int((n + 2) / 2)):
    if n % i == 0:
        if m > abs(i - n / i):
            ii = i
            m = abs(i - n / i)

jj = int(n / ii)

a, b = min(ii, jj), max(ii, jj)
print(a, b)
