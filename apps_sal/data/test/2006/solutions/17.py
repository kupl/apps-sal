'''
Created on 27.4.2016

@author: Ivan
'''
import sys


def main():
    line = input()
    parts = line.split(" ")
    a = int(parts[0])
    b = int(parts[1])
    list = []
    for i in range(0, a):
        list.append(input())
    pairs = []
    res = 0
    for l in list:
        x = l.find("G")
        y = l.find("S")
        print()
        if y < x:
            print("-1")
            return
        pairs.append((y - x))
    pairs = set(pairs)
    print(str(len(pairs)))


def __starting_point():
    main()


__starting_point()
