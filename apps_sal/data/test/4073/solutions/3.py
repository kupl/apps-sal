#!/usr/bin/env python3

def main():
    try:
        while True:
            input()
            a = list(map(int, input().split()))
            print(max(a) ^ a[-1])

    except EOFError:
        pass

main()

