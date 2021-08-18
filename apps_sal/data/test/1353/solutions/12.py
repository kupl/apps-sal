__author__ = 'sonerik'

import sys

inp = sys.stdin

all_drives, abon_drives, ord_price, abon_price = map(int, inp.readline().strip().split())


one_abon_price = abon_price / abon_drives


if one_abon_price < ord_price:
    abons = all_drives // abon_drives
    ords = all_drives % abon_drives

    if abon_price < ords * ord_price:
        abons += 1
        ords = 0

    print(abons * abon_price + ords * ord_price)
else:
    print(all_drives * ord_price)
