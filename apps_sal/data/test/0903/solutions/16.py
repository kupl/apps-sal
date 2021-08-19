n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
a = a[n // 2:]

n = n // 2 + 1
n_inc = 1


while m > 0:
    while n_inc < n and a[n_inc - 1] == a[n_inc]:
        n_inc += 1
    if n_inc == n:
        to_inc = m // n_inc
    else:
        to_inc = min(m // n_inc, a[n_inc] - a[n_inc - 1])

    total_inc = n_inc * to_inc

    #print(a, n_inc, to_inc, total_inc, m)

    m -= total_inc
    a[n_inc - 1] += to_inc

    if n_inc == n or to_inc == 0:
        break


print(a[n_inc - 1])
