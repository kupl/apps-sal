__author__ = 'sonerik'

import sys

inp = sys.stdin
# inp = open("a.txt")

all_drives, abon_drives, ord_price, abon_price = map(int, inp.readline().strip().split())

# print(all_drives, abon_drives, one_price, abon_price)

one_abon_price = abon_price / abon_drives

# print(one_abon_price, ord_price)

if one_abon_price < ord_price:  # abonement is better
    abons = all_drives // abon_drives
    ords = all_drives % abon_drives

    if abon_price < ords*ord_price:
        abons += 1
        ords = 0

    print(abons*abon_price + ords*ord_price)
else:
    print(all_drives*ord_price)
