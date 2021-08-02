n = int(input())
b = list(map(int, input().split()))
a = [0] * (2 * (len(b)))
a[-1] = b[0]
for i in range(1, len(b)):
    if b[i] - a[i - 1] <= a[-i]:
        a[i] = a[i - 1]
        a[-i - 1] = b[i] - a[i - 1]
    else:
        a[-i - 1] = a[-i]
        a[i] = b[i] - a[-i - 1]
print(*a)
