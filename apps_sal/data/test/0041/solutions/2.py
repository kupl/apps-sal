#!/usr/bin/env python3

def main():
    try:
        while True:
            n = int(input())
            a = list(map(int, input().split()))
            b = [0] * n
            last = 400000
            for i in range(n - 1, -1, -1):
                if a[i] == 0:
                    last = i
                b[i] = last - i

            last = -400000
            for i in range(n):
                if a[i] == 0:
                    last = i
                print(min(i - last, b[i]), end=' ')
            print()

    except EOFError:
        pass


main()
