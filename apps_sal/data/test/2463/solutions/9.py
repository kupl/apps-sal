n = int(input())
l = list(map(int, input().split()))
print((n - 1) // 2)
l.sort()
for i in range(n // 2):
    print(l[n - i - 1], end=' ')
    print(l[i], end=' ')
if n % 2 == 1:
    print(l[n // 2], end=' ')
print()
