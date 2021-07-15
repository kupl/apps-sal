#!/usr/bin/env python3

def main():
    import math

    try:
        while True:
            n = int(input())
            x = int(math.sqrt(n))
            while n % x:
                x -= 1
            print(x, n // x)

    except EOFError:
        pass

main()

