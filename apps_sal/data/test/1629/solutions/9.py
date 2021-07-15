def main():
    n, x = map(int,input().split())
    a = [int(i) for i in input().split()]
    j = x - 1
    z = min(a)
    while a[j] != z:
        if j == 0:
            j = n - 1
        else:
            j -= 1
    m = a[j]
    k = 0
    if x - 1 > j:
        for i in range(n):
            if j < i <= x - 1:
                a[i] -= (m + 1)
                k += (m + 1)
            else:
                a[i] -= m
                k += m
        a[j] += k
    elif x - 1 < j:
        for i in range(n):
            if x - 1 < i <= j:
                a[i] -= m
                k += m
            else:
                a[i] -=(m + 1)
                k += (m + 1)
        a[j] += k
    else:
        for i in range(n):
            a[i] -= m
            k += m
        a[j] += k
    print(*a)
main()
