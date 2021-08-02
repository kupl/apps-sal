import math
from sys import stdin
from math import ceil


def __starting_point():
    s = input()
    n = int(input())
    dictionary = {}

    for i in s:
        if i in dictionary:
            dictionary[i] = dictionary[i] + 1
        else:
            dictionary[i] = 1

    if len(dictionary) > n:
        print(-1)
    else:
        if len(s) < n:
            print(1)
            newS = s
        else:
            lengthS = len(s) // n
            newLength = len(s)
            while lengthS < newLength:
                mid = (lengthS + newLength) // 2
                total = 0
                for i in dictionary:
                    total = total + ceil(dictionary[i] / mid)
                if total > n:
                    lengthS = mid + 1
                else:
                    newLength = mid
            print(lengthS)
            newS = ''
            for i in dictionary:
                for j in range(ceil(dictionary[i] / lengthS)):
                    newS = newS + i
        for i in range(n - len(newS)):
            newS = newS + s[0]
        print(newS)


__starting_point()
