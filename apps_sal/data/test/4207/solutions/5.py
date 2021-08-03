from decimal import Decimal as mag, getcontext

getcontext().prec = 100


def main():
    n = int(input())
    arr = list(map(mag, input().split()))
    brr = list(map(mag, input().split()))
    mp = dict()
    mp[0] = 0
    pl = 0
    for i in range(n):
        if (arr[i] == 0 and brr[i] == 0):
            pl += 1
        if arr[i] == 0:
            continue
        k = - brr[i] / arr[i]
        mp[k] = mp.get(k, 0) + 1
    print(pl + max(mp.values()))


main()
