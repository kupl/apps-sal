#!/usr/bin/env python3

try:
    while True:
        n = int(input())
        a = b = 0
        for i in range(n):
            x, y = list(map(int, input().split()))
            if x > y:
                a += 1
            elif y > x:
                b += 1

        if a > b:
            print("Mishka")
        elif b > a:
            print("Chris")
        else:
            print("Friendship is magic!^^")

except EOFError:
    pass
