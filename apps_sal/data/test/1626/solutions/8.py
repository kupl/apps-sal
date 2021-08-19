(n, k) = [int(i) for i in input().split()]
sum = 1
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
for i in range(n // k):
    if n == 0:
        x = (10 ** k - 1) // a[i] - ((b[i] + 1) * 10 ** (k - 1) - 1) // a[i]
    else:
        x = (10 ** k - 1) // a[i] - ((b[i] + 1) * 10 ** (k - 1) - 1) // a[i] + (b[i] * 10 ** (k - 1) - 1) // a[i] + 1
    sum *= x
    sum %= 10 ** 9 + 7
print(sum)
