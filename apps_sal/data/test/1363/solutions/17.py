import math
def main():
    g, d, f = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    lst3 = list(map(int, input().split()))
    lst0 = []
    precounted = []
    ans = 0

    lst0 += [(c, 1) for c in lst1]
    lst0 += [(c, 2) for c in lst2]
    lst0 += [(c, 3) for c in lst3]

    lst0.sort()

    for i in range(len(lst0)):

        if len(precounted) == 0:
            a1, a2, a3 = (0, 0, 0)
        else:
            a1, a2, a3 = precounted[len(precounted) - 1]

        if (lst0[i][1] == 1):
            a1 += 1
        elif (lst0[i][1] == 2):
            a2 += 1
        else:
            a3 += 1

        precounted.append((a1, a2, a3))

        def product(iterable):
            prod = 1
            for n in iterable:
                prod *= n
            return prod

        def npr(n, r):
            assert 0 <= r <= n
            return product(range(n - r + 1, n + 1))

        def ncr(r, n):
            if r > n:
                return 0
            assert 0 <= r <= n
            if r > n // 2:
                r = n - r
            return npr(n, r) // math.factorial(r)

    for i in range(len(lst0) - 1):
        l = i + 1
        r = len(lst0)
        while l + 1 < r:
            m = (l + r) // 2
            if lst0[i][0] * 2 >= lst0[m][0]:
                l = m
            else:
                r = m
        max_possible_num = lst0[l][0]
        max_possible_ind = l

        a1 = precounted[max_possible_ind][0] - precounted[i][0]
        a2 = precounted[max_possible_ind][1] - precounted[i][1]
        a3 = precounted[max_possible_ind][2] - precounted[i][2]
        n1 = 1
        n2 = 2
        n3 = 3

        if lst0[i][1] == 1:
            n1 -= 1
        elif lst0[i][1] == 2:
            n2 -= 1
        else:
            n3 -= 1
        ans += ncr(n1, a1) * ncr(n2, a2) * ncr(n3, a3)

    print(ans)

main()
