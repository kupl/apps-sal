n = int(input())
a = list(map(int, input().split(' ')))
for i in range(n // 2):
    if not i & 1:
        (a[i], a[-i - 1]) = (a[-i - 1], a[i])
print(' '.join(map(str, a)))
