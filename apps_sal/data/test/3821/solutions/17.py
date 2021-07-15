from decimal import Decimal as fr


ans = 0

n = int(input())
a = list(map(fr, input().split()))

ans = max(a)


def calc(lst):
    nonlocal ans

    prod = 1
    for i in range(len(lst)):
        prod *= 1 - lst[i]
        cur = 0
        for j in range(i + 1):
            cur += lst[j] * prod / (1 - lst[j])

#        print(cur)
        ans = max(ans, cur)


lst = list(sorted([x for x in a if x < 0.5]))

calc(lst)
calc(lst[::-1])


print('{:.15f}'.format(ans))

