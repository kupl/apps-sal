n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a = sorted(a)
b = sorted(b)
c = sorted(c)


def lower_bound(arr, x):
    l = 0
    r = len(c)
    for j in range(30):
        mid = (l + r) // 2
        if x <= arr[mid]:
            r = mid
        else:
            l = mid
    return r


count = 0
for i in range(n):
    a_count = lower_bound(a, b[i])
    c_count = len(c) - lower_bound(c, b[i] + 1)
    count += a_count * c_count

print(count)
