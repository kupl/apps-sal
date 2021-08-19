n = int(input())
arr_a = []
arr_b = []
for i in range(n):
    (a, b) = map(int, input().split())
    arr_a.append(a)
    arr_b.append(b)
arr_a.sort()
arr_b.sort()
if n % 2 == 1:
    print(arr_b[n // 2] - arr_a[n // 2] + 1)
else:
    median_a = arr_a[int(n / 2 - 1)] + arr_a[int(n / 2)]
    median_b = arr_b[int(n / 2 - 1)] + arr_b[int(n / 2)]
    print(median_b - median_a + 1)
