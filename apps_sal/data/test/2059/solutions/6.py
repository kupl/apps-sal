n = int(input())
a = list(map(int, input().split()))
max1 = float('inf')
for q in range(len(a)):
    if q >= n-q-1:
        max1 = min(max1, min(a[q], a[0])//q)
    if q <= n-q-1:
        max1 = min(max1, min(a[q], a[-1]) // (n-q-1))
print(max1)

