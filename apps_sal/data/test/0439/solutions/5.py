#!/usr/bin/env python3

def main():
    n = int(input())
    m = int(input())
    print(m % (1 << n) if m >> n else m)

try:
    while True:
        main()
except EOFError:
    pass

