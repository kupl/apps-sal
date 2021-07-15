#!/usr/bin/env python3

def main():
    try:
        while True:
            for i in range(int(3e7)):
                pass
            print(*sorted(map(int, input().split()[1:])))

    except EOFError:
        pass

main()

