# coding: utf-8
import sys
sys.setrecursionlimit(int(1e7))


def main():
    n = int(input().strip())
    print(2 * (n * (n - 1)) + 1)
    return


while 1:
    try: main()
    except EOFError: break
