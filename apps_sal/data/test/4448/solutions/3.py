import math
from collections import defaultdict
import sys


def main():
    (n, m) = list(map(int, input().split()))
    k = list(map(int, input().split()))
    sales = [(0, 0)] * m
    for i in range(m):
        (a, b) = list(map(int, input().split()))
        sales[i] = (b, a)

    def check(days):
        last_sale = {}
        for sale in sales:
            if sale[1] <= days:
                if sale[0] not in last_sale or sale[1] > last_sale[sale[0]]:
                    last_sale[sale[0]] = sale[1]
        date_last_sales = {}
        for (t, d) in list(last_sale.items()):
            if d not in date_last_sales:
                date_last_sales[d] = [t]
            else:
                date_last_sales[d].append(t)
        balance = 0
        required = [0] + k.copy()
        end = 0
        for d in range(1, days + 1):
            balance += 1
            if d in date_last_sales:
                for t in date_last_sales[d]:
                    if required[t] > 0:
                        if required[t] > balance:
                            end += required[t] - balance
                        balance -= min(required[t], balance)
                        required[t] = 0
            if d == days:
                for r in required:
                    if r > 0:
                        end += r
        return 2 * end <= balance
    total = sum(k)
    for i in range(1, 2 * total + 1):
        if check(i):
            print(i)
            break


def __starting_point():
    main()


__starting_point()
