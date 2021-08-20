import sys
import math


def main():
    (a, b) = map(int, input().split())
    (c, d) = map(int, input().split())
    arr = list()
    dr = 0
    for i in range(0, 202):
        arr.append(b + dr * a)
        arr.append(d + dr * c)
        dr += 1
    arr = sorted(arr)
    for i in range(0, len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return print(arr[i])
    print(-1)


main()
