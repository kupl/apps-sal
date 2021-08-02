n = int(input())
a = list(map(int, input().split()))

c = 0

for i in range(n):
    if a[i] % 2 == 0:
        while a[i] % 2 == 0:
            a[i] /= 2
            c += 1

print(c)
