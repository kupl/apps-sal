n = int(input())

a = list(map(int, input().split()))

for i in range(n // 2):
    if i % 2 == 0:
        a[i], a[-i - 1] = a[-i - 1], a[i]

print(*a)

