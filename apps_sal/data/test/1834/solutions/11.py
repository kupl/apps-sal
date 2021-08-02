n = int(input())
ar = list(map(int, input().split()))
ar.sort()
for i in range(n // 2):
    print(ar[i], end=' ')
    print(ar[n - 1 - i], end=' ')
if n % 2 == 1:
    print(ar[n // 2])
