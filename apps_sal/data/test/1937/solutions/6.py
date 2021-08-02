n = int(input())
b = list(map(int, input().split()))
a = [0] * n
c1 = 0; c2 = 10 ** 18
for i in range(n // 2):
    if b[i] - c1 <= c2:
        a[i] = c1
        a[-i - 1] = b[i] - c1
        c2 = b[i] - c1
    else:
        a[-i - 1] = c2
        a[i] = b[i] - c2
        c1 = b[i] - c2
print(' '.join(map(str, a)))
