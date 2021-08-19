raw = input().split()
n = int(raw[0])
s = int(raw[1])


def sum_digits(x):
    z = 0
    while x:
        z += x % 10
        x //= 10
    return z


i = s
count = 0
while i <= n:
    q = i - sum_digits(i)
    if q >= s:
        count = n - i + 1
        break
    else:
        i += 1
print(count)

# print(sum_digits(1))
