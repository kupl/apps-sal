n = int(input())
a = [int(i) for i in input().split()]
b = a[:]
a.sort()
one = a[n // 2 - 1]
two = a[n // 2]


def get_median(i):
    if b[i] <= one:
        return two
    return one


for i in range(n):
    print(get_median(i))
