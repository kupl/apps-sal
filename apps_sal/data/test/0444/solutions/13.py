import sys
import math


def read_int():
    return int(input().strip())


def read_int_list():
    return list(map(int, input().strip().split()))


def read_string():
    return input().strip()


def read_string_list(delim=" "):
    return input().strip().split(delim)

###### Author : Samir Vyas #######
###### Write Code Below    #######


n = read_int()

print(n)

for i in range(n):
    print(1, end=" ")
print()
