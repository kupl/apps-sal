# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mayank manish
#
# Created:
# Copyright:   (c) mayank manish
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import math


def main():
    pass


def __starting_point():
    main()


n, x = list(map(int, input().split()))
numbers = list(map(int, input().split()))
s = abs(sum(numbers))
res = math.ceil(s / x)
print(res)


__starting_point()
