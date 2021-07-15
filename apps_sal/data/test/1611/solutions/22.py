import sys
import re

def main():
    a = int(input())
    b = input().split()
    bb = []
    for num in b:
        bb.append(int(num))
    b = bb
    b.sort()
    c = b.pop()
    d = 0
    for num in b:
        d += num
    e = c - d + 1
    print(e)
    return

main()

