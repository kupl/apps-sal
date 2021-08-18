"""
Created on Tue Jul  3 16:02:31 2018

@author: Arsanuos
"""


def main():
    def rd(): return list(map(int, input().split()))
    n = int(input())
    arr = rd()
    h = [0] * 1000
    for item in arr:
        h[item] += 1
    print(max(h))


def __starting_point():
    main()


__starting_point()
