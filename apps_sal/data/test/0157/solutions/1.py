#!/usr/bin/env python3

def main():
    try:
        while True:
            a = int(input())
            b = int(input())
            c = int(input())
            x = min(a, b >> 1, c >> 2)
            print(x * 7)

    except EOFError:
        pass

main()

