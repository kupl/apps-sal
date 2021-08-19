import collections
import heapq


def main():
    T = int(input().strip())
    for _ in range(T):
        s = input().strip('0')
        print(s.count('0'))


main()
