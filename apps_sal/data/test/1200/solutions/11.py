n = int(input())
a = sorted([int(x) for x in input().split()])


def mcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


min_ = mcd(a[1] - a[0], a[2] - a[1])
for i in range(3, n):
    min_ = mcd(min_, a[i] - a[i - 1])
    if min_ == 1:
        break
count = 0

for i in range(1, n):
    count += (a[i] - a[i - 1]) // min_ - 1

print(count)
