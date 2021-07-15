from fractions import gcd

a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

g = gcd(a, c)

if (d - b) % g == 0:
    big_tab = [0 for _ in range(101 * 101)]
    for i in range(b, 101 * 101, a):
        big_tab[i] = 1

    for i in range(d, 101 * 101, c):
        if big_tab[i]:
            print(i)
            break

else:
    print(-1)

