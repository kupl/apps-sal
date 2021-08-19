(n, m) = map(int, list(input().split()))
min_v = n // 2 + n % 2
while min_v % m != 0:
    min_v += 1
if min_v > n:
    print('-1')
else:
    print(min_v)
