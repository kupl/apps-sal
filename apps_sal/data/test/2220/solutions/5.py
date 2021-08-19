def mi():
    return list(map(int, input().split()))


'\n6 9 2\n1 3 3 7 4 2\n'
(n, m, k) = mi()
a = list(mi())
a.sort(reverse=True)
t = k + 1
nop = m // t
rem = m % t
print(nop * (k * a[0] + a[1]) + rem * a[0])
