#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mayank manish
#
# Created:
# Copyright:   (c) mayank manish
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

def __starting_point():
    main()
n, x = list(map(int, input().split()))
numbers = list(map(int, input().split()))
s = abs(sum(numbers))
res = s // x
if s % x != 0:
    res += 1
print(res)


__starting_point()
