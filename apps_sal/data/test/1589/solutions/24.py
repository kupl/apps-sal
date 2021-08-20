(n, m) = list(map(int, input().split()))
total = 0
for i in range(n):
    arr = list(map(int, input().split()))
    j = 0
    while j < 2 * m:
        total += arr[j] or arr[j + 1]
        j += 2
print(total)
