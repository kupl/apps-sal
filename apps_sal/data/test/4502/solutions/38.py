n = int(input())
a = list(map(int, input().split()))

if n % 2 == 0:
    b = a[n - 1::-2] + a[::2]
else:
    b = a[n - 1::-2] + a[1::2]

print(*b)
