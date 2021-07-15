n, k = map(int, input().split())
a = list(map(int, input().split()))
maxi = 0
minimum = n
for i in range(len(a)):
    if n % a[i] < minimum:
        minimum = n % a[i]
        maxi = i

print(maxi + 1, n // a[maxi])
