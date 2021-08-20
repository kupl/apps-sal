import statistics
n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    (a[i], b[i]) = list(map(int, input().split()))
cen_a = statistics.median(a)
cen_b = statistics.median(b)
if n % 2 == 1:
    print(cen_b - cen_a + 1)
else:
    print(int((cen_b - cen_a) * 2 + 1))
